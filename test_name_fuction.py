import unittest

from name_function1 import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """тесты для 'name_functionq.py'"""
    def test_first_last_name(self):
        """Имена вида 'Janis Joplin' работают правильно?"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_middle_last_name(self):
        """Работают ли такие имена, как 'Wolfgang Amadeus Mozart'?"""
        formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
        
if __name__ == '__main__':
    unittest.main()