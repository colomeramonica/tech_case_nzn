import unittest
from tech.domain.entities import TechCaseEntity


class TestTechCaseUnit(unittest.TestCase):
    def setUp(self):
        self.valid_params = {
            'input': 'asdfzxascvdfnozebranetworkpoasoidfuizxdfzxascvdcvdcvdasdnznznzasdf'
        }

        self.invalid_params_using_numbers = {
            'input': '128034492485'
        }

        self.invalid_params_using_invalid_chars = {
            'input': 'abc---defrgh...ske'
        }

    def test_valid_params(self):
        case = TechCaseEntity.find_longest_word(**self.valid_params)
        self.assertEqual(
            case, 'asdfzxascvdfnozebranetworkpoasoidfuizxdfzxascvdcvdcvdasdnznznzasdf')

    def test_invalid_params_using_numbers(self):
        with self.assertRaises(TypeError):
            TechCaseEntity.find_longest_word(
                **self.invalid_params_using_numbers)

    def test_invalid_params_using_invalid_chars(self):
        with self.assertRaises(TypeError):
            TechCaseEntity.find_longest_word(
                **self.invalid_params_using_invalid_chars)
