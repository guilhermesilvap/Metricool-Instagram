# Bifrost

A Bifrost (Bifrosttech, @bifrost.tech) é uma empresa de desenvolvimento de software. Constrói **sites institucionais, landing pages, software sob medida e automação de processos** para pequenas e médias empresas. A promessa é uma engenharia só, do site ao sistema que roda a empresa.

Este design system descreve a marca para o Instagram. Ele foi montado a partir dos 8 posts de referência da Bifrost (`Bifrost-Instagram.pptx`). Qualquer pessoa ou agente que vá criar um post deve ler este README, depois **Voz e copywriting** e **Formatos do Instagram**.

## A marca em uma frase

Escura, precisa e calma. Títulos enormes em caixa alta, uma palavra em azul-céu, um único visual de produto (um site, um celular, um fluxo, um número) e um orbe azul de luz. Sem emoji, sem foto de banco de imagem, sem ilustração de pessoas.

## Fundamentos visuais

### Cor
- **60–70% ground** (`ground`, #131313). Todo post é escuro. Única exceção: o **post azul cheio** (gradiente `blue-bright` → `blue-mid` → `blue-deep`, em diagonal), usado no máximo 1 a cada 6 posts, para quebrar o feed.
- **Texto em `ink`** (#f0eee9, um off-white quente, nunca branco puro sobre o ground). Apoio em `ink-soft`, numeração e metadados em `ink-muted`.
- **Uma ideia em `sky`** (#7cc4fb) por post: a palavra-chave do título, o número grande ou a seta. Nunca duas cores de destaque.
- **`blue`** (#1f72d6) só em elementos de interface dentro dos mockups: o botão "Fale conosco", o chip ativo e a barra principal do gráfico.
- Não existe vermelho, verde, roxo ou gradiente arco-íris na marca. O "arco-íris" da Bifrost é só azul.

### Tipografia
- Família única: **Arial** (`--font-sans`). Títulos em peso regular (400) e caixa alta, com entrelinha apertada (0,92) e tracking negativo. O impacto vem do tamanho, não do negrito.
- Negrito (700) só no wordmark `BIFROST.`, no texto do CTA e em microtextos de mockup.
- Rótulos (`eyebrow`) em caixa alta e com tracking aberto (0,115em): categoria, contador, @BIFROST.TECH.
- Estilos: `stat`, `hero`, `title`, `title-md`, `lead`, `body`, `item`, `chip`, `wordmark`, `eyebrow`, `cta`, `caption`, `micro`. Os tamanhos estão em px para o canvas de 1080px de largura.

### O título em dois tons
O recurso mais reconhecível da marca: a frase em `ink`, e o final dela, que carrega a promessa, em `sky`.
- SUA EMPRESA ABERTA **24 HORAS**
- QUATRO FRENTES, **UMA ENGENHARIA SÓ**
- QUANDO PLANILHAS **NÃO DÃO MAIS CONTA**
- DO SITE AO SISTEMA QUE **RODA A EMPRESA**
- SUA EMPRESA MERECE UM SITE **À ALTURA**

O destaque fica quase sempre no fim, e é uma única sequência de palavras, nunca palavras soltas.

### O orbe e as órbitas (motivo da marca)
Um disco grande com gradiente radial-linear `orb-light` (0%) → `sky` (45%) → `blue` (100%), sangrando para fora de um canto do post (topo-direita ou base-centro). Ao redor dele, 1 ou 2 **anéis de órbita** finos em `line` (1,5px). Ele é a "ponte de luz" da Bifrost. Use um orbe por post, nunca dois do mesmo tamanho, e nunca coloque texto em cima dele.

### Mockups de produto
O visual de cada post é um pedaço de produto desenhado com formas planas, não um print real:
- **Janela de navegador**: card `surface`, borda `line`, raio `radius-lg`, 3 pontos na barra, URL `suaempresa.com.br` em `ink-muted`, linhas de texto como barras `ink`/`surface-2` e um botão `blue`.
- **Celular**: moldura `ink` com raio `radius-xl`, tela clara, botão `blue` "Quero um orçamento", com `shadow-float`.
- **Fluxo**: chips em escada ligados por conectores `line`. Etapa 1 em `surface`, etapa 2 em `blue`, etapa 3 em `ink`.
- **Gráfico**: barras `surface-2` crescendo para barras `sky` e `blue`.
- **Busca**: campo `surface` em pílula, com ícone de lupa e o texto digitado.
- **Antes → depois**: planilha caótica (grade `line`, células em vermelho-escuro apagado) → seta `sky` → painel organizado.

### Espaço e grade
- Margem lateral `margin-x` (88px) e margem vertical `margin-y` (96px) no feed.
- Cabeçalho fixo: `BIFROST.` à esquerda e eyebrow ou contador à direita, na mesma linha.
- Rodapé fixo: `@BIFROST.TECH` à esquerda e CTA à direita.
- Cards em grade com gutter `space-3` e padding `space-4`.
- Muito espaço vazio. Um post tem no máximo **título + 1 visual + até 2 linhas de apoio**.

### Iconografia
Não há biblioteca de ícones. Setas tipográficas (→) fazem o papel de ícone. Os "ícones" dos cards de serviço são mini-mockups (janela, celular, nós de fluxo, barras). Se precisar de um ícone, desenhe-o com traço de 2px em `ink` ou `sky`, cantos arredondados e sem preenchimento.

### Logo
O logo é tipográfico: **BIFROST.** em Arial Bold, caixa alta, tracking 0,028em, com ponto final. Não existe arquivo de símbolo. Escreva-o como texto no estilo `wordmark`, em `ink` (ou em `on-blue` no post azul).

## Componentes
- **CTA**: botão de chamada para ação, em dois estilos (contorno e sólido).
- **MolduraPost**: a moldura fixa do post (cabeçalho, rodapé e orbe), com um exemplo completo.
- **CardServico**: card das quatro frentes.
- **ChipFluxo**: etapas de um processo automatizado.
- **TituloDoisTons**: o título com destaque em sky.

## O que nunca fazer
- Fundo claro, bege ou branco em post de feed.
- Emoji, foto de banco de imagem, pessoas, mascotes, 3D brilhante.
- Gradiente roxo/rosa/neon ou "cara de IA".
- Mais de uma cor de destaque ou mais de um orbe.
- Título em minúsculas ou em negrito.
- Texto sobre o orbe.
- Mais de ~25 palavras de texto na arte de um post único.
