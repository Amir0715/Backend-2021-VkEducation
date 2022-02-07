import unittest
from utils.utils import levenshtein_distance


class LevensheinDistance(unittest.TestCase):
    """Класс тестов для функции расстояния Левенштейна
    """

    def test_eq_char_word(self):
        res = levenshtein_distance('A', 'A')
        self.assertEqual(res, 0)

    def test_empty_word(self):
        res = levenshtein_distance('A', '')
        self.assertEqual(res, 1)

    def test_empty_words(self):
        res = levenshtein_distance('', '')
        self.assertEqual(res, 0)

    def test_eq_whitespace_words(self):
        res = levenshtein_distance('    ', '    ')
        self.assertEqual(res, 4)

    def test_neq_whitespace_words(self):
        res = levenshtein_distance('       ', '     ')
        self.assertEqual(res, 6)

    def test_eq_word(self):
        res = levenshtein_distance('python', 'python')
        self.assertEqual(res, 0)

    def test_neq_word(self):
        res = levenshtein_distance('python', 'java')
        self.assertEqual(res, 6)

    def test_neq_r_word(self):
        res = levenshtein_distance('java', 'python')
        self.assertEqual(res, 6)
