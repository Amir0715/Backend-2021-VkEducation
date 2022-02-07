
class CustomList(list):
    """Класс расширения списка
    """


    def __add__(self, value: list[int]):
        arrmax = self if len(self) >= len(value) else value
        arrmin = self if len(self) < len(value) else value
        res = CustomList(arrmax)

        for i in range(len(arrmin)):
            res[i] = res[i] + arrmin[i]
        return res

    def __radd__(self, value: list[int]):
        return self.__add__(value)

    def __sub__(self, value: list[int]):
        arrmax = self if len(self) >= len(value) else value
        arrmin = self if len(self) < len(value) else value
        res = CustomList(arrmax)

        for i in range(len(arrmin)):
            res[i] = res[i] - arrmin[i]
        return res

    def __rsub__(self, value: list[int]):
        return self.__sub__(value)

    def __lt__(self, value: list[int]) -> bool:
        return sum(self) < sum(value)

    def __le__(self, value: list[int]) -> bool:
        return sum(self) <= sum(value)

    def __eq__(self, value: list[int]) -> bool:
        return sum(self) == sum(value)

    def __ne__(self, value: list[int]) -> bool:
        return sum(self) != sum(value)

    def __gt__(self, value: list[int]) -> bool:
        return sum(self) > sum(value)

    def __ge__(self, value: list[int]) -> bool:
        return sum(self) >= sum(value)
