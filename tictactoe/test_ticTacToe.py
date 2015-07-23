from unittest import TestCase
from tictactoe import TicTacToe

__author__ = 'phizaz'


class TestTicTacToe(TestCase):
    def test_winner(self):
        game = TicTacToe()
        assert game.winner() is None
        for i in range(3):
            game.turn((0, i))
            game.turn((1, i))
        assert game.winner() is 1
    def test_display(self):
        game = TicTacToe()
        for i in range(3):
            game.turn((0, i))
            game.turn((1, i))
        game.display()
        # assert 0
