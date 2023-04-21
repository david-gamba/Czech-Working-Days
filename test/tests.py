import unittest
from datetime import date, timedelta
from dateutil.easter import easter
from czech_workdays_holidays import get_holidays


class TestGetHolidays(unittest.TestCase):

    def test_dates_only(self):
        year = 2023
        expected_holidays = {date(year, 1, 1), easter(year) + timedelta(days=-2), easter(year) + timedelta(days=1),
                             date(year, 5, 1), date(year, 5, 8), date(year, 7, 5), date(year, 7, 6), date(year, 9, 28),
                             date(year, 10, 28), date(year, 11, 17), date(year, 12, 24), date(year, 12, 25),
                             date(year, 12, 26)}
        holidays = set(get_holidays(year, dates_only=True))
        self.assertSetEqual(holidays, expected_holidays)

class TestAssertRaises(unittest.TestCase):
    def test_year_type(self):
        with self.assertRaises(TypeError):
            get_holidays('2023')

    def test_dates_only_type(self):
        with self.assertRaises(TypeError):
            get_holidays(2023, dates_only='True')

    def test_dates_and_cz_names_type(self):
        with self.assertRaises(TypeError):
            get_holidays(2023, dates_and_cz_names=1)

    def test_dates_and_en_names_type(self):
        with self.assertRaises(TypeError):
            get_holidays(2023, dates_and_en_names=0)

    def test_shopping_restricted_type(self):
        with self.assertRaises(TypeError):
            get_holidays(2023, shopping_restricted='False')

    def test_year_value(self):
        with self.assertRaises(Exception):
            get_holidays(2000)

    def test_dates_only_output(self):
        holidays = get_holidays(2023, dates_only=True)
        for holiday in holidays:
            self.assertIsInstance(holiday, date)

    def test_dates_and_cz_names_output(self):
        holidays = get_holidays(2023, dates_and_cz_names=True)
        for holiday in holidays:
            self.assertIsInstance(holiday, list)
            self.assertIsInstance(holiday[0], date)
            self.assertIsInstance(holiday[1], str)

    def test_dates_and_en_names_output(self):
        holidays = get_holidays(2023, dates_and_en_names=True)
        for holiday in holidays:
            self.assertIsInstance(holiday, list)
            self.assertIsInstance(holiday[0], date)
            self.assertIsInstance(holiday[1], str)

    def test_shopping_restricted_output(self):
        holidays = get_holidays(2023, shopping_restricted=True)
        for holiday in holidays:
            self.assertTrue(holiday['shopping_restricted'])