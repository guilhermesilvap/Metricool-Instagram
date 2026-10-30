"""Busca fotos reais em alta definição no Pexels ou no Unsplash para os posts da Bifrost.

Chaves (nunca no repositório, que é público):
  PEXELS_API_KEY e/ou UNSPLASH_ACCESS_KEY, como variável de ambiente
  ou em linhas CHAVE=valor no arquivo ~/.bifrost-fotos.env

Uso:
  python3 ferramentas/foto.py buscar "termos em inglês" posts/<pasta> [--fonte pexels|unsplash] [--orientacao portrait|landscape|square] [--n 4]
      Baixa N candidatas para posts/<pasta>/_candidatas/cand-N.jpg (pasta ignorada pelo git)
      e grava os créditos em _candidatas/candidatas.json. Abra cada uma com a ferramenta de imagem antes de escolher.
  python3 ferramentas/foto.py escolher posts/<pasta> <N> <nome>
      Copia a candidata N para posts/<pasta>/<nome>.jpg e registra o crédito em posts/<pasta>/creditos.json.
  python3 ferramentas/foto.py creditos posts/<pasta>
      Imprime a linha de crédito para a legenda (ex.: "Fotos: Ana Lima / Pexels · João Reis / Unsplash").

Códigos de saída: 0 ok · 2 sem chave · 3 serviço inacessível (domínio bloqueado ou fora do ar) · 4 nenhuma foto boa.
"""
import json, os, pathlib, shutil, sys, urllib.parse, urllib.request
from PIL import Image

MIN_LADO = 1350          # menor lado aceitável para cobrir um post 1080x1350 sem ampliar
UA = "BifrostInstagramAgent/1.0"


def chaves():
    env = dict(os.environ)
    f = pathlib.Path.home() / ".bifrost-fotos.env"
    if f.exists():
        for linha in f.read_text().splitlines():
            if "=" in linha and not linha.strip().startswith("#"):
                k, v = linha.split("=", 1)
                env.setdefault(k.strip(), v.strip().strip('"'))
    return env.get("PEXELS_API_KEY"), env.get("UNSPLASH_ACCESS_KEY")


def get(url, headers=None, binario=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA, **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            dados = r.read()
    except Exception as e:  # proxy 403, DNS, timeout
        print(f"ERRO de rede em {urllib.parse.urlsplit(url).netloc}: {e}", file=sys.stderr)
        sys.exit(3)
    return dados if binario else json.loads(dados)


def buscar_pexels(chave, termos, orientacao, n):
    q = urllib.parse.urlencode({"query": termos, "orientation": orientacao, "per_page": max(n * 3, 15), "size": "large"})
    js = get(f"https://api.pexels.com/v1/search?{q}", {"Authorization": chave})
    out = []
    for p in js.get("photos", []):
        if min(p["width"], p["height"]) < MIN_LADO:
            continue
        out.append({
            "fonte": "Pexels", "id": p["id"], "autor": p["photographer"], "autor_url": p["photographer_url"],
            "pagina": p["url"], "alt": p.get("alt") or "",
            "baixar": p["src"]["original"] + "?auto=compress&cs=tinysrgb&w=2400",
            "ping": None,
        })
    return out[:n]


def buscar_unsplash(chave, termos, orientacao, n):
    ori = {"portrait": "portrait", "landscape": "landscape", "square": "squarish"}[orientacao]
    q = urllib.parse.urlencode({"query": termos, "orientation": ori, "per_page": max(n * 3, 15), "content_filter": "high"})
    js = get(f"https://api.unsplash.com/search/photos?{q}", {"Authorization": f"Client-ID {chave}", "Accept-Version": "v1"})
    out = []
    for p in js.get("results", []):
        if min(p["width"], p["height"]) < MIN_LADO or p.get("premium") or p.get("plus"):
            continue
        out.append({
            "fonte": "Unsplash", "id": p["id"], "autor": p["user"]["name"],
            "autor_url": p["user"]["links"]["html"] + "?utm_source=bifrost&utm_medium=referral",
            "pagina": p["links"]["html"], "alt": p.get("alt_description") or "",
            "baixar": p["urls"]["raw"] + "&w=2400&q=85&fm=jpg&fit=max",
            "ping": p["links"]["download_location"],
        })
    return out[:n]


def cmd_buscar(args):
    termos, pasta = args[0], pathlib.Path(args[1])
    opts = {"--fonte": None, "--orientacao": "portrait", "--n": "4"}
    for i in range(2, len(args) - 1, 2):
        opts[args[i]] = args[i + 1]
    pk, uk = chaves()
    fonte = opts["--fonte"] or ("pexels" if pk else "unsplash" if uk else None)
    chave = {"pexels": pk, "unsplash": uk}.get(fonte)
    if not chave:
        print("Sem chave do Pexels/Unsplash (PEXELS_API_KEY ou UNSPLASH_ACCESS_KEY).", file=sys.stderr)
        sys.exit(2)
    achadas = (buscar_pexels if fonte == "pexels" else buscar_unsplash)(chave, termos, opts["--orientacao"], int(opts["--n"]))
    if not achadas:
        print("Nenhuma foto com resolução suficiente. Tente outros termos (em inglês, concretos: 'dentist clinic reception').", file=sys.stderr)
        sys.exit(4)
    dest = pasta / "_candidatas"
    dest.mkdir(parents=True, exist_ok=True)
    for i, c in enumerate(achadas, 1):
        arq = dest / f"cand-{i}.jpg"
        arq.write_bytes(get(c["baixar"], binario=True))
        im = Image.open(arq).convert("RGB")
        im.save(arq, quality=90)
        c["arquivo"], c["tamanho"] = arq.name, list(im.size)
        print(f"{arq}  {im.size[0]}x{im.size[1]}  {c['fonte']} · {c['autor']} · {c['alt'][:70]}")
    (dest / "candidatas.json").write_text(json.dumps(achadas, ensure_ascii=False, indent=1))


def cmd_escolher(args):
    pasta, n, nome = pathlib.Path(args[0]), int(args[1]), args[2]
    cands = json.loads((pasta / "_candidatas" / "candidatas.json").read_text())
    c = cands[n - 1]
    destino = pasta / f"{nome}.jpg"
    shutil.copy(pasta / "_candidatas" / c["arquivo"], destino)
    if c.get("ping"):  # exigência da API do Unsplash: registrar o download
        pk, uk = chaves()
        get(c["ping"], {"Authorization": f"Client-ID {uk}"})
    cred_f = pasta / "creditos.json"
    creditos = json.loads(cred_f.read_text()) if cred_f.exists() else {}
    creditos[destino.name] = {k: c[k] for k in ("fonte", "id", "autor", "autor_url", "pagina")}
    cred_f.write_text(json.dumps(creditos, ensure_ascii=False, indent=1))
    print(destino, "←", c["fonte"], c["autor"])


def cmd_creditos(args):
    cred = json.loads((pathlib.Path(args[0]) / "creditos.json").read_text())
    vistos = []
    for c in cred.values():
        s = f"{c['autor']} / {c['fonte']}"
        if s not in vistos:
            vistos.append(s)
    print(("Foto: " if len(vistos) == 1 else "Fotos: ") + " · ".join(vistos))


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("buscar", "escolher", "creditos"):
        sys.exit(__doc__)
    {"buscar": cmd_buscar, "escolher": cmd_escolher, "creditos": cmd_creditos}[sys.argv[1]](sys.argv[2:])
