[🇺🇸 English](README.md) · **🇧🇷 Português (Brasil)**

# Jogo da Velha

> **Status:** Concluído
> **Engine / Biblioteca:** Nenhuma (somente console)
> **Linguagem:** Python 3.11+ (somente biblioteca padrão)

## Proposta

O jogo da velha clássico 3x3, jogado no console contra outro humano ou contra o computador. O jogador 1 escolhe X ou O, os jogadores alternam os turnos digitando uma célula como `A1` ou `C3`, e a tela é limpa após cada jogada. Um placar no topo registra as vitórias de cada jogador e os empates durante a sessão, e depois de cada rodada os jogadores podem começar outra. O jogo inteiro é um único arquivo, `tic_tac_toe.py`.

O computador tem dois níveis de dificuldade, ambos usando a mesma função minimax com poda alfa-beta: o **Normal** olha só duas jogadas à frente (vence ou bloqueia quando vê uma ameaça direta, mas pode ser enganado com um garfo) e o **Difícil** pesquisa a árvore inteira do jogo, então nunca perde.

O menu permite trocar o idioma da interface entre inglês e português do Brasil; todo o texto exibido ao jogador fica em um só lugar.

"Concluído" significa: dois humanos conseguem jogar rodadas completas com placar, e um adversário com o computador baseado no algoritmo minimax pode ser selecionado no menu.

## Habilidades que pretendo praticar

- **Arrays 2D:** o tabuleiro é uma lista de listas 3x3; converter a entrada no estilo `A1` para `[linha][coluna]` e verificar linhas, colunas e diagonais.
- **Lógica de turnos:** alternar jogadores e quem começa, tratar jogadas inválidas e repetidas, detectar vitórias e empates.
- **Algoritmo minimax:** busca recursiva pela melhor jogada do computador, pontuando vitórias pela profundidade, poda alfa-beta e um limite de profundidade para criar um nível mais fraco.

## Escopo

- **Essencial:** menu, modo para 2 jogadores, escolha de X/O, tabuleiro no console, limpeza de tela, placar da sessão, pergunta para jogar de novo, textos em inglês e português, jogar contra o computador (Normal e Difícil).
- **Extras:** nenhum planejado.
- **Fora do escopo:** gráficos, som, rede, salvar placar em disco, testes automatizados.

## Como rodar

```bash
python tic_tac_toe.py
```

No menu, escolha "Jogar (2 jogadores humanos)" ou "Jogar contra o computador" (depois Normal ou Difícil). Digite uma célula como letra da coluna seguida do número da linha (`A1`, `b2`, `C3`). Digite `Q` durante uma rodada para voltar ao menu.

## Capturas de tela / GIFs

_A adicionar._

## O que aprendi

_A preencher após terminar._
