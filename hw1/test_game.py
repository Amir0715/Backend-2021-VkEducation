import unittest

from game import TicTacGame
from exceptions import CellOccupiedError, InvalidInputError


class TestTicTacGame(unittest.TestCase):
    """Класс тестов для игры крестики-нолики
    """

    def setUp(self) -> None:
        self.game = TicTacGame()

    def test_validation_positiv(self):
        """Тест на ввод валидных значений в [1, 9]
        """

        user_inputs = [str(i) for i in range(1, 10)]
        for user_input in user_inputs:
            with self.subTest(user_input=user_input):
                res = self.game._validation(user_input)
                self.assertTrue(res, "Should be 'True' ")

    def test_valid_input_positiv(self):
        """Тест на ввод не валидных значений не в [1, 9]
        """

        user_inputs = ['-2', '-1', '0', '10', '11', '12']
        for user_input in user_inputs:
            with self.subTest(user_input=user_input):
                with self.assertRaises(
                    InvalidInputError,
                    msg=f"Значение {user_input} должно было вызывать исключение ValueError"
                ):
                    self.game._validation(user_input)

    def test_valid_input_char_negative(self):
        """Тест на ввод не валидных символов
        """

        user_inputs = ['a', 'ф', '!', 'd11']
        for user_input in user_inputs:
            with self.subTest(user_input=user_input):
                with self.assertRaises(
                    ValueError,
                    msg=f"Значение {user_input} должно было вызывать исключение ValueError"
                ):
                    self.game._validation(user_input)

    def test_valid_input_cell_occupied_negative(self):
        """Тест на ввод номера занятой клетки
        """

        user_inputs = ['1']
        self.game._board[0] = self.game.X
        for user_input in user_inputs:
            with self.assertRaises(
                CellOccupiedError,
                msg=f"Значение {user_input} для занятой ячейки должно было вызывать исключение CellOccupiedError"
            ):
                self.game._validation(user_input)

    def test_check_winner(self):
        """Тест на проверку победителя
        """
        X = self.game.X
        O = self.game.O

        # Случай:
        #
        #
        #
        self.assertFalse(
            self.game._check_winner(),
            f"Для доски \n: {self.game._board} не должно быть победителя"
        )

        # Случай:
        # X X X
        # O O
        #
        self.game._board = [X] * 3 + [O] * 2 + [" "] * 3
        self.assertTrue(
            self.game._check_winner(),
            f"Для доски \n: {self.game._board} должен быть победитель"
        )

        # Случай:
        # X O
        # X O
        # X
        self.game._board = [X, O, " "] * 2 + [X, " ", " "]
        self.assertTrue(
            self.game._check_winner(),
            f"Для доски \n: {self.game._board} должен быть победитель"
        )

        # Случай:
        # X O
        #   X
        #   O X
        self.game._board = [" "] * 9
        self.game._board[0] = X
        self.game._board[1] = O
        self.game._board[4] = X
        self.game._board[7] = X
        self.game._board[8] = X
        self.assertTrue(
            self.game._check_winner(),
            f"Для доски \n: {self.game._board} должен быть победитель"
        )

        # Случай:
        # O O X
        #   X
        # X
        self.game._board = [" "] * 9
        self.game._board[0] = O
        self.game._board[1] = O
        self.game._board[2] = X
        self.game._board[4] = X
        self.game._board[6] = X
        self.assertTrue(
            self.game._check_winner(),
            f"Для доски \n: {self.game._board} должен быть победитель"
        )

        # Случай:
        # O X X
        # X X O
        # O O X
        self.game._board = [O, X, X] + [X, X, O] + [O, O, X]
        self.assertFalse(
            self.game._check_winner(),
            f"Для доски \n: {self.game._board} не должно быть победителя"
        )
