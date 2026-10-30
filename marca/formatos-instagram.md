# Formatos do Instagram

## Tamanhos
| Formato | Canvas | Área segura |
| --- | --- | --- |
| Post único | 1080 × 1350 (4:5) | margens `margin-x` 88px / `margin-y` 96px |
| Carrossel | 1080 × 1350 por slide, de 5 a 7 slides | a mesma; o contador `01 / 05` fica no cabeçalho, à direita |
| Stories | 1080 × 1920 (9:16) | 250px livres no topo e 340px livres na base (interface do Instagram) |

## Anatomia de um post de feed
1. **Cabeçalho** (y = 96): `BIFROST.` à esquerda; eyebrow com o serviço ou contador à direita.
2. **Eyebrow** opcional acima do título (ex.: SITES INSTITUCIONAIS).
3. **Título em dois tons**, estilo `title` ou `hero`.
4. **Visual principal**: um mockup ou um número `stat`.
5. **Apoio** opcional: lista de 3 itens numerados ou até 2 linhas de `body`.
6. **Rodapé** (y = 1350 − 96): `@BIFROST.TECH` à esquerda e CTA à direita.
7. **Orbe + órbitas** sangrando de um canto, atrás de tudo.

## Layouts de referência
- **Promessa + navegador**: título no topo-esquerda, orbe no topo-direita, janela de navegador no meio e rodapé com CTA em contorno.
- **Azul cheio + celular**: gradiente azul diagonal, título branco, lista 01-02-03 à esquerda e celular à direita. Rodapé sem CTA.
- **Grade 2×2 de serviços**: título no topo e quatro CardServico. CTA sólido no rodapé.
- **Número gigante**: campo de busca flutuando sobre o orbe, `stat` em sky, `lead` explicando e `caption` com a fonte.
- **Carrossel**: capa com visual antes → depois no topo e título hero na base; slides internos com fluxo em chips no topo, número, título-md e corpo; slide final com título enorme, CTA sólido e orbe na base.
- **Carrossel foto** (`modelos/foto-exemplo.html`): capa com foto em tela cheia, véu e título hero na base; slides internos com foto recortada (y 200–720), número, título-md (76px) e corpo; fechamento com foto escurecida (`.veu-forte`) e CTA.
- **Carrossel editorial / Tech da semana** (`modelos/editorial-exemplo.html`): capa com tag "TECH DA SEMANA · datas", foto recortada e título hero; cada notícia com tag do tema, foto 16:9 (y 290–710), manchete (68px), "O que muda:" e fonte + data no rodapé; fechamento pedindo para seguir.

## Stories
- Mesmo cabeçalho, mas descido para y = 250.
- Eyebrow com a oferta (ORÇAMENTO SEM CUSTO), título `title` em dois tons.
- Visual (navegador + celular sobre o orbe) no centro.
- **Nunca** reserve espaço para figurinha (a API não as adiciona). O chamado vai escrito na arte.
- Com foto (`modelos/story-foto-exemplo.html`): **notícia do dia** (foto inteira + véu + manchete a partir de y≈1020) e **isso ou aquilo** (foto nos 900px de cima, pergunta e dois cards A/B embaixo).
- Sem rodapé @BIFROST.TECH, porque o perfil já aparece no topo do story.
