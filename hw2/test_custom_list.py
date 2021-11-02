import unittest

from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    """Класс тестов для CustomList
    """

    def test_add_custom_eq_len(self):
        """Тест сложения двух объектов CustomList равной длины
        """

        a = CustomList([i for i in range(1, 10)])
        b = CustomList([j for j in range(9, 0, -1)])
        res = CustomList([10 for _ in range(1, 10)])
        c = a + b
        self.assertListEqual(c, res)
        self.assertIsInstance(c, CustomList)

    def test_add_custom_ne_len(self):
        """Тест сложения двух объектов CustomList разной длины 
        """

        a = CustomList([i for i in range(1, 5)])
        b = CustomList([j for j in range(9, 0, -1)])
        res = CustomList([10, 10, 10, 10, 5, 4, 3, 2, 1])
        c = a + b
        self.assertListEqual(c, res)
        self.assertIsInstance(c, CustomList)

    def test_add_list_eq_len(self):
        """Тест сложения объекта CustomList и list() равно длины 
        """

        a = CustomList([i for i in range(1, 10)])
        b = [j for j in range(9, 0, -1)]
        res = CustomList([10 for _ in range(1, 10)])
        c = a + b
        self.assertListEqual(c, res)
        self.assertIsInstance(c, CustomList)

    def test_add_list_ne_len(self):
        """Тест сложения объекта CustomList и list() разной длины 
        """

        a = CustomList([i for i in range(1, 5)])
        b = [j for j in range(9, 0, -1)]
        res = CustomList([10, 10, 10, 10, 5, 4, 3, 2, 1])
        c = a + b
        self.assertListEqual(c, res)
        self.assertIsInstance(c, CustomList)

    def test_radd_custom_eq_len(self):
        """Тест праввого сложения двух объектов CustomList равной длины
        """

        a = CustomList([i for i in range(1, 10)])
        b = CustomList([j for j in range(9, 0, -1)])
        res = CustomList([10 for _ in range(1, 10)])
        c = b + a
        self.assertListEqual(c, res)
        self.assertIsInstance(c, CustomList)

    def test_radd_custom_ne_len(self):
        """Тест праввого сложения двух объектов CustomList разной длины 
        """

        a = CustomList([i for i in range(1, 5)])
        b = CustomList([j for j in range(9, 0, -1)])
        res = CustomList([10, 10, 10, 10, 5, 4, 3, 2, 1])
        c = b + a
        self.assertListEqual(c, res)
        self.assertIsInstance(c, CustomList)

    def test_radd_list_eq_len(self):
        """Тест праввого сложения объекта CustomList и list() равно длины 
        """

        a = CustomList([i for i in range(1, 10)])
        b = [j for j in range(9, 0, -1)]
        res = CustomList([10 for _ in range(1, 10)])
        c = b + a
        self.assertListEqual(c, res)
        self.assertIsInstance(c, CustomList)

    def test_radd_list_ne_len(self):
        """Тест праввого сложения объекта CustomList и list() разной длины 
        """

        a = CustomList([i for i in range(1, 5)])
        b = [j for j in range(9, 0, -1)]
        res = CustomList([10, 10, 10, 10, 5, 4, 3, 2, 1])
        c = b + a
        self.assertListEqual(c, res)
        self.assertIsInstance(c, CustomList)

    def test_lt_custom(self):
        """Тест оператора меньше для двух объектов CustomList
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = CustomList([j for j in range(1, 5)])  # sum = 15
        self.assertLess(b, a)
    
    def test_lt_list(self):
        """Тест оператора меньше объекта CustomList и list
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = [j for j in range(1, 5)] # sum = 15
        self.assertLess(b, a)

    def test_le_custom_equel(self):
        """Тест оператора меньше или равно для двух равных объектов CustomList
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = CustomList([j for j in range(1, 10)])  # sum = 45
        self.assertLessEqual(b, a)
    
    def test_le_list_equel(self):
        """Тест оператора меньше или равно для равных объекта CustomList и list
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = [j for j in range(1, 10)] # sum = 45
        self.assertLessEqual(b, a)

    def test_le_custom_nonequel(self):
        """Тест оператора меньше или равно для двух не равных объектов CustomList
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = CustomList([j for j in range(1, 5)])  # sum = 15
        self.assertLessEqual(b, a)
    
    def test_le_list_nonequel(self):
        """Тест оператора меньше или равно для не равных объекта CustomList и list
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = [j for j in range(1, 5)] # sum = 15
        self.assertLessEqual(b, a)

    def test_eq_custom(self):
        """Тест оператора равно для двух объектов CustomList
        """

        a = CustomList([i for i in range(1, 11)])  # sum = 45 
        b = CustomList([5 for j in range(11)])  # sum = 45
        self.assertEqual(a, b)
    
    def test_eq_list(self):
        """Тест оператора равно объекта CustomList и list
        """

        a = CustomList([i for i in range(1, 11)])  # sum = 45 
        b = [5 for j in range(11)] # sum = 45
        self.assertEqual(a, b)

    def test_ne_custom(self):
        """Тест оператора равно для двух не равных объектов CustomList
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = CustomList([j for j in range(1, 5)])  # sum = 15
        self.assertNotEqual(a, b)
    
    def test_ne_list(self):
        """Тест оператора равно для не равных объекта CustomList и list
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = [j for j in range(1, 5)] # sum = 15
        self.assertNotEqual(a, b)
    
    def test_gt_custom(self):
        """Тест оператора больше для двух объектов CustomList
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = CustomList([j for j in range(1, 5)])  # sum = 15
        self.assertGreater(a, b)
    
    def test_gt_list(self):
        """Тест оператора больше объекта CustomList и list
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = [j for j in range(1, 5)] # sum = 15
        self.assertGreater(a, b)

    def test_ge_custom_equel(self):
        """Тест оператора больше или равно для двух равных объектов CustomList
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = CustomList([j for j in range(1, 10)])  # sum = 45
        self.assertGreaterEqual(a, b)
    
    def test_ge_list_equel(self):
        """Тест оператора больше или равно для равных объекта CustomList и list
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = [j for j in range(1, 10)] # sum = 45
        self.assertGreaterEqual(a, b)

    def test_ge_custom_nonequel(self):
        """Тест оператора больше или равно для двух не равных объектов CustomList
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = CustomList([j for j in range(1, 5)])  # sum = 15
        self.assertGreaterEqual(a, b)
    
    def test_ge_list_nonequel(self):
        """Тест оператора больше или равно для не равных объекта CustomList и list
        """

        a = CustomList([i for i in range(1, 10)])  # sum = 45 
        b = [j for j in range(1, 5)] # sum = 15
        self.assertGreaterEqual(a, b)
