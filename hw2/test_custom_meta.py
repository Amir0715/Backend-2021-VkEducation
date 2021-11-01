import unittest

from custom_meta import CustomClass

class TestCustomMeta(unittest.TestCase):
    """Класс теста для мета класса CustomMeta
    """

    def test_name_atr_without_param(self):
        """Тест на то что имена методов и атрибутов начинается с custom_ 
        """

        inst = CustomClass()
        self.assertTrue(hasattr(inst, 'custom_val'))
        self.assertTrue(hasattr(inst, 'custom_x'))
        self.assertTrue(hasattr(inst, 'custom_line'))
        self.assertFalse(hasattr(inst, 'val'))
        self.assertFalse(hasattr(inst, 'x'))
        self.assertFalse(hasattr(inst, 'line'))

    def test_name_atr_with_param(self):
        """Тест на то что имена методов и атрибутов начинается с custom_ 
        """

        inst = CustomClass(123)
        self.assertTrue(hasattr(inst, 'custom_val'))
        self.assertTrue(hasattr(inst, 'custom_x'))
        self.assertTrue(hasattr(inst, 'custom_line'))
        self.assertFalse(hasattr(inst, 'val'))
        self.assertFalse(hasattr(inst, 'x'))
        self.assertFalse(hasattr(inst, 'line'))

    def test_name_atr_with_kwparam(self):
        """Тест на то что имена методов и атрибутов начинается с custom_ 
        """

        inst = CustomClass(val=123)
        self.assertTrue(hasattr(inst, 'custom_val'))
        self.assertTrue(hasattr(inst, 'custom_x'))
        self.assertTrue(hasattr(inst, 'custom_line'))
        self.assertFalse(hasattr(inst, 'val'))
        self.assertFalse(hasattr(inst, 'x'))
        self.assertFalse(hasattr(inst, 'line'))