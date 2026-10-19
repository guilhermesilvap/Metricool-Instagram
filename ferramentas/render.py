"""Renderiza um HTML de post da Bifrost em JPGs prontos para o Instagram.

Uso:  python3 ferramentas/render.py posts/<pasta>/arte.html
Cada elemento .slide (1080x1350) ou .story (1080x1920) vira posts/<pasta>/slide-N.jpg,
na ordem em que aparece. O HTML deve linkar ../../ferramentas/marca.css.
"""
import sys, pathlib
from PIL import Image
from playwright.sync_api import sync_playwright

html = pathlib.Path(sys.argv[1]).resolve()
out = html.parent
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto(html.as_uri()); pg.wait_for_timeout(400)
    els = pg.query_selector_all(".slide, .story")
    if not els:
        sys.exit("Nenhum .slide ou .story encontrado no HTML.")
    for i, el in enumerate(els, 1):
        png = out / f"_tmp-{i}.png"
        el.screenshot(path=str(png))
        im = Image.open(png).convert("RGB")
        assert im.size in [(1080, 1350), (1080, 1920)], f"tamanho inesperado {im.size} no item {i}"
        im.save(out / f"slide-{i}.jpg", quality=88, optimize=True)
        png.unlink()
        print(out / f"slide-{i}.jpg", im.size)
    b.close()
