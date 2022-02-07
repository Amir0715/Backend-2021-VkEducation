from os import system, name
from typing import Union
from collections import deque

from exceptions import InvalidInputError, CellOccupiedError

def clear():
    """Функция для очистки консоли
    """

    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
class TicTacGame:
    """Класс игры крестики-нолики
    """

    _turn = 0  # Идекс хода

    X = "X"  # Первый игрок играет Х
    O = "O"  # Второй игрок играет O

    _stack_error: deque[str] = deque()

    def __init__(self):
        n = 3  # размер поля

        self._n = n
        self._max_turns = n * n  # Максимальный индекс хода
        self._board = [' ' for _ in range(n * n)]  # Создаем поле размером n*n

        self._game_info = f"Поля пронумерованны с 1 до {n*n} начиная с левого верхнего края. \
                            \nВ [] указан игрок который должен сходить \
                            \n----------------------------------------------------------------"

    def _print_board(self):
        """Выводит доску в консоль
        """

        board = ""
        for i in range(self._n * self._n):
            board += f" {self._board[i]} |"
            if (i + 1) % self._n == 0:
                board += f"\n{'--- ' * self._n}\n"

        print(board)

    def _print_info(self):
        """Вводить информацию об игре
        """

        print(self._game_info)
        while len(self._stack_error):
            print(self._stack_error.pop())

    def _check_winner(self) -> bool:
        """Проверка победителя
        Если хотя бы одна строка, столбец или диагональ
        заполнена одинаковым элементом вернется True
        иначе False
        """

        n = self._n

        for i in range(n):
            # Проверка строк и стобцов
            row = self._board[i*n:(i+1)*n]  # срез по строкам
            col = self._board[i::n]  # срез по столбцам

            for stok in [row, col]:
                res_X = all(elem == self.X for elem in stok)
                res_O = all(elem == self.O for elem in stok)

                if res_X or res_O:
                    return True

        # Проверка диагоналей
        diagonal = self._board[::n+1]
        r_diagonal = self._board[n-1:n*n-1:n-1]
        for stok in [diagonal, r_diagonal]:
            res_X = all(elem == self.X for elem in stok)
            res_O = all(elem == self.O for elem in stok)

            if res_X or res_O:
                return True

        return False

    def _valid_input(self) -> Union[int, None]:
        """Возвращает валидное значение полученное с консоли

        Если было получено не валидное значение возбуждается исключение

        Исключения:
        -----------
        ValueError: если было введено не число
        EOFError: если пользователь нажал ctrl+d
        KeyboardInterrupt: если пользователь нажал ctrl+c

        """

        player = self.X if self._turn % 2 == 0 else self.O
        value = input(f"[{player}] Введите номер клетки для вставки: ")
        if self._validation(value):
            return int(value)

        return None

    def _validation(self, value: str) -> bool:
        """Проверка значения на валидность

        Args:
            value (str): значение

        Raises:
            InvalidInputError: если значение больше допустимых
            CellOccupiedError: если клетка была уже занята

        Returns:
            bool: валидно или нет
        """

        intvalue = int(value)

        if intvalue <= 0 or intvalue > self._n * self._n:
            raise InvalidInputError(
                f"Значение должно > 0 и <= {self._n * self._n}!")

        if self._board[intvalue - 1] != ' ':
            raise CellOccupiedError(
                f"Клетка под номером {intvalue} занята игроком [{self._board[intvalue - 1]}]")

        return True

    def run(self):
        """Запуск цикла игры
        """

        while True:
            # Игра продолжается пока нет победителя
            try:
                clear()
                self._print_info()
                self._print_board()

                if self._turn >= self._max_turns:
                    print("Ничья!")
                    break

                value = self._valid_input()
                if value is not None:
                    self._board[value - 1] = (
                        self.X if self._turn % 2 == 0 else self.O
                    )
                    self._turn += 1

                    if self._check_winner():
                        clear()
                        self._print_info()
                        self._print_board()
                        print(
                            f"Выиграл игрок [{self.X if self._turn % 2 == 1 else self.O}]")
                        break

            except CellOccupiedError as e:
                self._stack_error.append(str(e))

            except InvalidInputError as e:
                self._stack_error.append(str(e))

            except ValueError:
                self._stack_error.append("Значение должно быть числом!")

            except EOFError:
                print("\nПока!")
                break

            except KeyboardInterrupt:
                print("\nПока!")
                break
