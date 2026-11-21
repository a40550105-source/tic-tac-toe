"""A simple two-player terminal tic-tac-toe game."""

from typing import Optional, Sequence


WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def get_winner(board: Sequence[Optional[str]]) -> Optional[str]:
    """Return the winning mark, or None if the board has no winner."""
    for first, second, third in WINNING_LINES:
        mark = board[first]
        if mark is not None and mark == board[second] == board[third]:
            return mark
    return None


def is_draw(board: Sequence[Optional[str]]) -> bool:
    """Return whether the board is full and has no winner."""
    return get_winner(board) is None and all(cell is not None for cell in board)


def display_board(board: Sequence[Optional[str]]) -> None:
    """Print the board, showing cell numbers wherever a move can be made."""
    cells = [str(index + 1) if mark is None else mark for index, mark in enumerate(board)]
    print(f"\n {cells[0]} | {cells[1]} | {cells[2]}")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]}")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]}\n")


def play_game() -> None:
    """Run a complete game, prompting two players to take turns."""
    board: list[Optional[str]] = [None] * 9
    current_player = "X"

    while True:
        display_board(board)
        choice = input(f"Player {current_player}, choose a cell (1-9): ").strip()
        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Please enter a number from 1 to 9.")
            continue

        cell = int(choice) - 1
        if board[cell] is not None:
            print("That cell is already taken. Choose another one.")
            continue

        board[cell] = current_player
        winner = get_winner(board)
        if winner is not None:
            display_board(board)
            print(f"Player {winner} wins!")
            return
        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            return

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()
