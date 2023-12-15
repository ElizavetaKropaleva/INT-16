import unittest
from custom_title import *


class TestCustomTitle(unittest.TestCase):
    # Тест 1: Обычная строка
    def test_usual_line(self):
        input_str = 'Строка для тестирования пользовательской функции title'
        result = custom_title(input_str)
        self.assertEqual(result, input_str.title())

    # Тест 2: Строка с различными разделителями
    def test_string_with_different_separators(self):
        input_str = ' разные,разделители   между\t\tсловами '
        result = custom_title(input_str)
        self.assertEqual(result, input_str.title())

    # Тест 3: Строка с числами и спецсимволами
    def test_string_with_numbers_and_special_characters(self):
        input_str = '123 это -1 тестовая & строка!'
        result = custom_title(input_str)
        self.assertEqual(result, input_str.title())
