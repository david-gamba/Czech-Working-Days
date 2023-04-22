import unittest
from datetime import date, timedelta
from dateutil.easter import easter
from czech_workdays_holidays import get_holidays, get_workdays, get_shopping_days, get_holidays_during_weekend
from random import randint


class TestGetHolidays(unittest.TestCase):

    def test_dates_only(self):
        year = 2023
        expected_holidays = {date(year, 1, 1), easter(year) + timedelta(days=-2), easter(year) + timedelta(days=1),
                             date(year, 5, 1), date(year, 5, 8), date(year, 7, 5), date(year, 7, 6), date(year, 9, 28),
                             date(year, 10, 28), date(year, 11, 17), date(year, 12, 24), date(year, 12, 25),
                             date(year, 12, 26)}
        holidays = set(get_holidays(year, dates_only=True))
        self.assertSetEqual(holidays, expected_holidays)

    def test_good_friday_before_2016(self):
        year = randint(2001, 2015)
        expected_holidays = {date(year, 1, 1), easter(year) + timedelta(days=1),
                             date(year, 5, 1), date(year, 5, 8), date(year, 7, 5), date(year, 7, 6), date(year, 9, 28),
                             date(year, 10, 28), date(year, 11, 17), date(year, 12, 24), date(year, 12, 25),
                             date(year, 12, 26)}
        holidays = set(get_holidays(year, dates_only=True))
        self.assertSetEqual(holidays, expected_holidays)

    def test_shopping_restriction_during_2016(self):
        year = 2016
        expected_holidays = {date(year, 10, 28), date(year, 12, 25), date(year, 12, 26)}
        holidays = set(get_holidays(year, dates_only=True,shopping_restricted=True))
        self.assertSetEqual(holidays, expected_holidays)

    def test_holidays_during_weekend_2023(self):
        year = 2023
        expected_holidays = [date(2023, 1, 1), date(2023, 1, 1), date(2023, 10, 28), date(2023, 12, 24)]
        holidays = get_holidays_during_weekend(2023)
        self.assertEqual(expected_holidays, holidays)


    def test_dates_and_cz_names(self):
        year = 2023
        expected_holidays = [[date(year, 1, 1), 'Den obnovy samostatného českého státu'],
                             [date(year, 1, 1), 'Nový Rok'],
                             [easter(year) + timedelta(days=-2), 'Velký pátek'],
                             [easter(year) + timedelta(days=1), 'Velikonoční pondělí'],
                             [date(year, 5, 1), 'Svátek práce'],
                             [date(year, 5, 8), 'Den vítězství'],
                             [date(year, 7, 5), 'Den slovanských věrozvěstů Cyrila a Metoděje'],
                             [date(year, 7, 6), 'Den upálení mistra Jana Husa'],
                             [date(year, 9, 28), 'Den české státnosti'],
                             [date(year, 10, 28), 'Den vzniku samostatného československého státu'],
                             [date(year, 11, 17), 'Den boje za svobodu a demokracii a Mezinárodní den studentstva'],
                             [date(year, 12, 24), 'Štědrý den'],
                             [date(year, 12, 25), '1. svátek vánoční'],
                             [date(year, 12, 26), '2. svátek vánoční']]
        holidays = get_holidays(year, dates_and_cz_names=True)
        self.assertEqual(holidays, expected_holidays)

    def test_dates_and_en_names(self):
        year = 2023
        expected_holidays = [[date(year, 1, 1), 'Restoration Day of the Independent Czech State'],
                            [date(year, 1, 1), "New Year's Day"],
                            [easter(year) + timedelta(days=-2), 'Good Friday'],
                            [easter(year) + timedelta(days=1), 'Easter Monday'],
                            [date(year, 5, 1), 'Labour Day'],
                            [date(year, 5, 8), 'Victory Day'],
                            [date(year, 7, 5), 'Saints Cyril and Methodius Day'],
                            [date(year, 7, 6), 'Jan Hus Day'],
                            [date(year, 9, 28), 'Czech Statehood Day'],
                            [date(year, 10, 28), 'Czechoslovak Independence State Day'],
                            [date(year, 11, 17), "Struggle for freedom and democracy and International Student Day"],
                            [date(year, 12, 24), 'Christmas Eve'],
                            [date(year, 12, 25), 'Christmas Day'],
                            [date(year, 12, 26), "St. Stephen's Day"]]
        holidays = get_holidays(year, dates_and_en_names=True)
        self.assertEqual(holidays, expected_holidays)


class TestGetWorkdays(unittest.TestCase):
    def test_get_workdays_2023(self):
        year = 2023
        expected_number = 250

        result = len(get_workdays(2023))
        self.assertEqual(result, expected_number)

    def test_get_workdays_2023_with_sundays(self):
        year = 2023
        sundays = 53
        holidays_in_sunday = 2
        expected_number = 250 + sundays - holidays_in_sunday

        result = len(get_workdays(2023, include_sunday=True))
        self.assertEqual(expected_number, result)

    def test_get_workdays_2023_with_saturdays(self):
        year = 2023
        saturdays = 52
        holidays_in_saturday = 1
        expected_number = 250 + saturdays - holidays_in_saturday

        result = len(get_workdays(2023, include_saturday=True))
        self.assertEqual(expected_number, result)


class TestGetShoppingDays(unittest.TestCase):
    def test_shopping_restriction_before_2016(self):
        year = randint(2001, 2015)

        expected_result = Exception("Shopping resctriction came into effect 01/10/2016 (DD/MM/YY)")

        with self.assertRaises(Exception):
            get_holidays(year, shopping_restricted=True)


class TestAssertRaises(unittest.TestCase):

    # Get holidays
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

    def test_year_value_get_holidays(self):
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

    # Get workdays
    def test_get_workdays(self):
        # Test case 1: Year must be an integer
        try:
            get_workdays("2023")
        except TypeError as e:
            assert str(e) == "Year must be an integer."

        # Test case 2: include_saturday must be a boolean
        try:
            get_workdays(2023, include_saturday="True")
        except TypeError as e:
            assert str(e) == "include_saturday must be a boolean."

        # Test case 3: include_sunday must be a boolean
        try:
            get_workdays(2023, include_sunday="True")
        except TypeError as e:
            assert str(e) == "include_sunday must be a boolean."

        # Test case 4: include_holidays must be a boolean
        try:
            get_workdays(2023, include_holidays="True")
        except TypeError as e:
            assert str(e) == "include_holidays must be a boolean."

    # Get shopping days
    def test_year_type_exception(self):
        with self.assertRaises(TypeError):
            get_shopping_days("2023")

    def test_include_saturday_type_exception(self):
        with self.assertRaises(TypeError):
            get_shopping_days(2023, include_saturday="True")

    def test_include_sunday_type_exception(self):
        with self.assertRaises(TypeError):
            get_shopping_days(2023, include_sunday=1)

    def test_exclude_shopping_restricted_days_type_exception(self):
        with self.assertRaises(TypeError):
            get_shopping_days(2023, exclude_shopping_restriced_days=0)

    # Get holidays during weekend
    def test_get_holidays_during_weekend_year_type_exception(self):
        # Test case 1: Year must be an integer
        try:
            get_holidays_during_weekend("2023")
        except TypeError as e:
            assert str(e) == "Year must be an integer."
