import unittest
from DataSanitizer import *
# from consolidate_data import fix_cell_format

class DataTestCase(unittest.TestCase):

    def test_remove_first_space_from_tel(self):
        result = remove_first_space_from_tel(" 988123453")
        self.assertEqual(result, "988123453")

    def test_remove_plus_from_tel(self):
       result = remove_plus_from_tel("+99312132")
       self.assertEqual(result, "99312132")

    def test_remove_country_code1(self):
        result = remove_country_code("464646")
        self.assertEqual(result, "4646")

    def test_remove_country_code2(self):
        result = remove_country_code("0463333")
        self.assertEqual(result, "3333")
    def test_remove_country_code3(self):
        result = remove_country_code("00463333")
        self.assertEqual(result, "3333")
    def test_remove_country_code3(self):
        result = remove_country_code("003333")
        self.assertEqual(result, "3333")

    def test_place_zero_at_first(self):
        result = place_zero_at_first("99312132")
        self.assertEqual(result, "099312132")

    def test_remove_all_characters(self):
       result = remove_all_characters("09+öä'+9312*13..2")
       self.assertEqual(result, "099312132")


    def test_fix_telephone_format(self):
        result = fix_telephone_format("+004609+öä'+9312*13..2")
        self.assertEqual(result, "099312132")