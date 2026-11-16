**🇺🇸 English** · [🇧🇷 Português (Brasil)](README-ptbr.md)

# Tic-Tac-Toe

> **Status:** In Progress
> **Engine / Library:** None (console only)
> **Language:** Python 3.11+ (standard library only)

## Proposal

The classic 3x3 game for two human players, played in the console. Player 1 picks X or O, the players alternate turns by typing a cell such as `A1` or `C3`, and the screen is cleared after every move. A scoreboard at the top tracks each player's wins and the draws during the session, and after every round the players can start another one. The whole game is a single file, `tic_tac_toe.py`.

The menu lets the player switch the interface language between English and Brazilian Portuguese; all player-facing text is kept in one place.

"Done" means: two humans can play full rounds with a scoreboard, and a computer opponent based on the minimax algorithm can be selected from the menu.

## Skills I expect to practice

- **2D arrays:** the board is a 3x3 list of lists; translating `A1`-style input into `[row][col]` and checking rows, columns and diagonals.
- **Turn logic:** alternating players and starters, handling invalid and repeated moves, detecting wins and draws.
- **Minimax algorithm:** recursive search for the computer's best move (planned).

## Scope

- **Must have:** menu, 2-player mode, X/O choice, console board, screen clearing, session scoreboard, play-again prompt, English and Portuguese texts.
- **Stretch goals:** play against the computer using minimax (next step).
- **Out of scope:** graphics, sound, networking, saving scores to disk, automated tests.

## How to run

```bash
python tic_tac_toe.py
```

Type a cell as column letter plus row number (`A1`, `b2`, `C3`). Type `Q` during a round to go back to the menu.

## Screenshots / GIFs

_To be added._

## What I learned

_To be filled in after finishing._
