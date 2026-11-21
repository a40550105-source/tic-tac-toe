import unittest

from main import get_winner, is_draw


class BoardOutcomeTests(unittest.TestCase):
    def test_detects_winning_row(self):
        self.assertEqual(get_winner(["X", "X", "X", "O", None, "O", None, None, None]), "X")

    def test_detects_winning_diagonal(self):
        self.assertEqual(get_winner(["O", "X", "X", None, "O", None, "X", None, "O"]), "O")

    def test_no_winner_on_incomplete_board(self):
        self.assertIsNone(get_winner(["X", "O", "X", None, "O", None, None, None, "X"]))

    def test_full_board_without_winner_is_draw(self):
        self.assertTrue(is_draw(["X", "O", "X", "X", "O", "O", "O", "X", "X"]))

    def test_winning_full_board_is_not_draw(self):
        self.assertFalse(is_draw(["X", "X", "X", "O", "O", "X", "X", "O", "O"]))


if __name__ == "__main__":
    unittest.main()
