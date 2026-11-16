"""Tic-tac-toe for two human players, played in the console.

Single-file game, standard library only. Run with: python tic_tac_toe.py

Skills practiced: 2D arrays (the board), turn logic (alternating players and
rounds) and, later, the minimax algorithm (computer opponent).

The file is organized in sections:
    1. Texts        - every player-facing string, per language
    2. Board logic  - pure functions on a 3x3 list of lists
    3. Console UI   - clearing the screen, drawing, reading input
    4. Game flow    - a round, a session of rounds, and the main menu
"""

from __future__ import annotations

import os

# --------------------------------------------------------------------------- #
# 1. Texts
# --------------------------------------------------------------------------- #

LANGUAGES = {"en": "English", "pt": "Português (Brasil)"}

STRINGS = {
    "en": {
        "title": "=== TIC-TAC-TOE ===",
        "menu_play_2p": "Play (2 human players)",
        "menu_language": "Change language",
        "menu_quit": "Quit",
        "menu_prompt": "Choose an option: ",
        "invalid_option": "Invalid option.",
        "language_title": "=== LANGUAGE ===",
        "language_prompt": "Choose a language: ",
        "language_changed": "Language changed to English.",
        "choose_symbol": "Player 1, do you want to be X or O? ",
        "invalid_symbol": "Please type X or O.",
        "player_1": "Player 1",
        "player_2": "Player 2",
        "scoreboard": "Score",
        "draws": "Draws",
        "turn_prompt": "{player} ({symbol}), your move (e.g. A1, Q to quit): ",
        "first_move": "{player} ({symbol}) starts the round.",
        "moved": "{player} ({symbol}) played {cell}.",
        "invalid_move": "Invalid move. Use a column A-C and a row 1-3, like B2.",
        "occupied": "That cell is already taken. Choose another one.",
        "win": "{player} ({symbol}) wins the round!",
        "draw": "It's a draw!",
        "play_again": "Play another round? (y/n): ",
        "yes_answers": ("y", "yes"),
        "back_to_menu": "Back to the menu.",
        "goodbye": "Thanks for playing!",
        "press_enter": "Press Enter to continue...",
    },
    "pt": {
        "title": "=== JOGO DA VELHA ===",
        "menu_play_2p": "Jogar (2 jogadores humanos)",
        "menu_language": "Mudar idioma",
        "menu_quit": "Sair",
        "menu_prompt": "Escolha uma opção: ",
        "invalid_option": "Opção inválida.",
        "language_title": "=== IDIOMA ===",
        "language_prompt": "Escolha um idioma: ",
        "language_changed": "Idioma alterado para Português (Brasil).",
        "choose_symbol": "Jogador 1, você quer ser X ou O? ",
        "invalid_symbol": "Digite X ou O.",
        "player_1": "Jogador 1",
        "player_2": "Jogador 2",
        "scoreboard": "Placar",
        "draws": "Empates",
        "turn_prompt": "{player} ({symbol}), sua jogada (ex.: A1, Q para sair): ",
        "first_move": "{player} ({symbol}) começa a rodada.",
        "moved": "{player} ({symbol}) jogou em {cell}.",
        "invalid_move": "Jogada inválida. Use uma coluna A-C e uma linha 1-3, como B2.",
        "occupied": "Essa casa já está ocupada. Escolha outra.",
        "win": "{player} ({symbol}) venceu a rodada!",
        "draw": "Deu empate!",
        "play_again": "Jogar outra rodada? (s/n): ",
        "yes_answers": ("s", "sim"),
        "back_to_menu": "Voltando ao menu.",
        "goodbye": "Obrigado por jogar!",
        "press_enter": "Pressione Enter para continuar...",
    },
}


class Texts:
    """Looks up player-facing strings in the selected language."""

    def __init__(self, language: str = "en") -> None:
        self.language = language

    def get(self, key: str, **kwargs: str) -> str:
        text = STRINGS[self.language][key]
        return text.format(**kwargs) if kwargs else text

    def is_yes(self, answer: str) -> bool:
        return answer.strip().lower() in STRINGS[self.language]["yes_answers"]


# --------------------------------------------------------------------------- #
# 2. Board logic (pure: no input() or print())
# --------------------------------------------------------------------------- #

SIZE = 3
EMPTY = " "
COLUMNS = "ABC"

Board = list[list[str]]


def new_board() -> Board:
    return [[EMPTY] * SIZE for _ in range(SIZE)]


def parse_cell(text: str) -> tuple[int, int] | None:
    """Turn 'A1' into (row, col) = (0, 0). Returns None if the text is invalid."""
    text = text.strip().upper()
    if len(text) != 2:
        return None
    letter, number = text[0], text[1]
    if letter not in COLUMNS or number not in "123":
        return None
    return int(number) - 1, COLUMNS.index(letter)


def cell_name(row: int, col: int) -> str:
    return f"{COLUMNS[col]}{row + 1}"


def check_winner(board: Board) -> str | None:
    """Return the winning symbol, or None if nobody has won (yet)."""
    lines = [list(row) for row in board]
    lines += [[board[r][c] for r in range(SIZE)] for c in range(SIZE)]
    lines.append([board[i][i] for i in range(SIZE)])
    lines.append([board[i][SIZE - 1 - i] for i in range(SIZE)])
    for line in lines:
        if line[0] != EMPTY and line.count(line[0]) == SIZE:
            return line[0]
    return None


def is_full(board: Board) -> bool:
    return all(cell != EMPTY for row in board for cell in row)


def other_symbol(symbol: str) -> str:
    return "O" if symbol == "X" else "X"


# --------------------------------------------------------------------------- #
# 3. Console UI
# --------------------------------------------------------------------------- #


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def render_board(board: Board) -> str:
    header = "  " + " ".join(f" {letter} " for letter in COLUMNS)
    separator = "  " + "+".join("---" for _ in range(SIZE))
    lines = [header]
    for index, row in enumerate(board):
        lines.append(f"{index + 1} " + "|".join(f" {cell} " for cell in row))
        if index < SIZE - 1:
            lines.append(separator)
    return "\n".join(lines)


def render_scoreboard(texts: Texts, session: Session) -> str:
    p1, p2 = session.p1_symbol, other_symbol(session.p1_symbol)
    return (
        f"{texts.get('scoreboard')}: "
        f"{texts.get('player_1')} ({p1}): {session.wins[p1]} | "
        f"{texts.get('player_2')} ({p2}): {session.wins[p2]} | "
        f"{texts.get('draws')}: {session.draws}"
    )


def draw_screen(texts: Texts, session: Session, board: Board, message: str) -> None:
    clear_screen()
    print(render_scoreboard(texts, session))
    print()
    print(render_board(board))
    print()
    if message:
        print(message)


# --------------------------------------------------------------------------- #
# 4. Game flow
# --------------------------------------------------------------------------- #


class Session:
    """What lasts across rounds: who is X/O, the score and who starts."""

    def __init__(self, p1_symbol: str) -> None:
        self.p1_symbol = p1_symbol
        self.wins = {"X": 0, "O": 0}
        self.draws = 0
        self.starter = "X"  # X starts the first round; the starter then alternates

    def player_name(self, texts: Texts, symbol: str) -> str:
        key = "player_1" if symbol == self.p1_symbol else "player_2"
        return texts.get(key)


def ask_symbol(texts: Texts) -> str:
    while True:
        answer = input(texts.get("choose_symbol")).strip().upper()
        if answer in ("X", "O"):
            return answer
        print(texts.get("invalid_symbol"))


def play_round(texts: Texts, session: Session) -> tuple[Board, str | None, bool]:
    """Play one round. Returns (board, winner symbol or None for a draw, quit?)."""
    board = new_board()
    current = session.starter
    name = session.player_name(texts, current)
    message = texts.get("first_move", player=name, symbol=current)

    while True:
        draw_screen(texts, session, board, message)
        name = session.player_name(texts, current)
        answer = input(texts.get("turn_prompt", player=name, symbol=current))
        if answer.strip().upper() == "Q":
            return board, None, True

        cell = parse_cell(answer)
        if cell is None:
            message = texts.get("invalid_move")
            continue
        row, col = cell
        if board[row][col] != EMPTY:
            message = texts.get("occupied")
            continue

        board[row][col] = current
        winner = check_winner(board)
        if winner is not None:
            return board, winner, False
        if is_full(board):
            return board, None, False

        message = texts.get(
            "moved", player=name, symbol=current, cell=cell_name(row, col)
        )
        current = other_symbol(current)


def play_session(texts: Texts) -> None:
    clear_screen()
    session = Session(ask_symbol(texts))

    while True:
        board, winner, quit_requested = play_round(texts, session)
        if quit_requested:
            return

        if winner is None:
            session.draws += 1
            result = texts.get("draw")
        else:
            session.wins[winner] += 1
            result = texts.get(
                "win", player=session.player_name(texts, winner), symbol=winner
            )

        draw_screen(texts, session, board, result)
        if not texts.is_yes(input(texts.get("play_again"))):
            return
        session.starter = other_symbol(session.starter)


def choose_language(texts: Texts) -> None:
    codes = list(LANGUAGES)
    while True:
        clear_screen()
        print(texts.get("language_title"))
        for number, code in enumerate(codes, start=1):
            print(f"{number}) {LANGUAGES[code]}")
        answer = input(texts.get("language_prompt")).strip()
        if answer.isdigit() and 1 <= int(answer) <= len(codes):
            texts.language = codes[int(answer) - 1]
            return


def main() -> None:
    texts = Texts("en")
    while True:
        clear_screen()
        print(texts.get("title"))
        print(f"1) {texts.get('menu_play_2p')}")
        print(f"2) {texts.get('menu_language')}")
        print(f"3) {texts.get('menu_quit')}")
        choice = input(texts.get("menu_prompt")).strip()

        if choice == "1":
            play_session(texts)
        elif choice == "2":
            choose_language(texts)
        elif choice == "3":
            print(texts.get("goodbye"))
            return
        else:
            print(texts.get("invalid_option"))
            input(texts.get("press_enter"))


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
