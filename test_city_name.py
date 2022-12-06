import unittest

from city_function import city_function


class Test_city(unittest.TestCase):
    """тесты для 'city_fuction.py"""
    def test_city_country(self):
        """тестирование названий города и страны "Paris - France"""
        formatted_city_country = city_function('paris','france')
        self.assertEqual(formatted_city_country,'Paris - France')
    def test_city_country_population(self):
        """тестирование названий города и страны "Paris - France: 500000"""
        formatted_city_country = city_function('paris','france','500000')
        self.assertEqual(formatted_city_country, 'Paris - France: 500000')
if __name__ == '__main__':
    unittest.main()