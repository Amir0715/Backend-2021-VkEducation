
class CostumList(list):
    """Класс расширения списка
    """


    def __add__(self, value: list[int]):
        arrmax = self if len(self) >= len(value) else value
        arrmin = self if len(self) < len(value) else value
        res = CostumList(arrmax)

        for i in range(len(arrmin)):
            res[i] = res[i] + arrmin[i]
        return res

    def __radd__(self, value: list[int]):
        arrmax = self if len(self) >= len(value) else value
        arrmin = self if len(self) < len(value) else value
        res = CostumList(arrmax)

        for i in range(len(arrmin)):
            res[i] = res[i] + arrmin[i]
        return res

    def __sub__(self, value: list[int]):
        arrmax = self if len(self) >= len(value) else value
        arrmin = self if len(self) < len(value) else value
        res = CostumList(arrmax)

        for i in range(len(arrmin)):
            res[i] = res[i] - arrmin[i]
        return res

    def __rsub__(self, value: list[int]):
        arrmax = self if len(self) >= len(value) else value
        arrmin = self if len(self) < len(value) else value
        res = CostumList(arrmax)

        for i in range(len(arrmin)):
            res[i] = res[i] - arrmin[i]
        return res

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


if __name__ == "__main__":
    a = CostumList([1, 2, 3, 4])
    b = CostumList([1, 2, 3, 4])
    d = [2] * 10
    c = a + b
    c = b + a
    # print(a, "+", b, "=", c)
    # print(sum(d), sum(b), d > b)
    print(sum(a), sum(b), a == b)
    print(sum(d), sum(b), d == b)


