**🇺🇸 English** · [🇧🇷 Português (Brasil)](README-ptbr.md)

# Tic-Tac-Toe

> **Status:** In Progress
> **Engine / Library:** None (console only)
> **Language:** Python 3.11+ (standard library only)

## Proposal

The classic 3x3 game, played in the console against another human or against the computer. Player 1 picks X or O, the players alternate turns by typing a cell such as `A1` or `C3`, and the screen is cleared after every move. A scoreboard at the top tracks each player's wins and the draws during the session, and after every round the players can start another one. The whole game is a single file, `tic_tac_toe.py`.

The computer has two difficulty levels, both powered by the same minimax function with alpha-beta pruning: **Normal** looks only two moves ahead (it wins or blocks when it sees a direct threat, but can be tricked with a fork) and **Hard** searches the whole game tree, so it never loses.

The menu lets the player switch the interface language between English and Brazilian Portuguese; all player-facing text is kept in one place.

"Done" means: two humans can play full rounds with a scoreboard, and a computer opponent based on the minimax algorithm can be selected from the menu.

## Skills I expect to practice

- **2D arrays:** the board is a 3x3 list of lists; translating `A1`-style input into `[row][col]` and checking rows, columns and diagonals.
- **Turn logic:** alternating players and starters, handling invalid and repeated moves, detecting wins and draws.
- **Minimax algorithm:** recursive search for the computer's best move, scoring wins by depth, alpha-beta pruning, and a depth limit to build a weaker difficulty level.

## Scope

- **Must have:** menu, 2-player mode, X/O choice, console board, screen clearing, session scoreboard, play-again prompt, English and Portuguese texts, play against the computer (Normal and Hard).
- **Stretch goals:** none planned.
- **Out of scope:** graphics, sound, networking, saving scores to disk, automated tests.

## How to run

```bash
python tic_tac_toe.py
```

From the menu, pick "Play (2 human players)" or "Play against the computer" (then Normal or Hard). Type a cell as column letter plus row number (`A1`, `b2`, `C3`). Type `Q` during a round to go back to the menu.

## Screenshots / GIFs

_To be added._

## What I learned

_To be filled in after finishing._
