
from datetime import timedelta, date
from dateutil.easter import easter


def get_holidays(year):
    holidays = (
        {
            "holiday_name_cz": "Den obnovy samostatného českého státu",
            "holiday_name_en": "Restoration Day of the Independent Czech State",
            "date": date(year, 1, 1),
            "fixed": True,
            "public_other": "State",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Nový Rok",
            "holiday_name_en": "New Year's Day",
            "date": date(year, 1, 1),
            "fixed": True,
            "public_other": "Other",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Svátek práce",
            "holiday_name_en": "Labor Day",
            "date": date(year, 5, 1),
            "fixed": True,
            "public_other": "Other",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Den vítězství",
            "holiday_name_en": "Victory Day",
            "date": date(year, 5, 8),
            "fixed": True,
            "public_other": "Public",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Den slovanských věrozvěstů Cyrila a Metoděje",
            "holiday_name_en": "Saints Cyril and Methodius Day",
            "date": date(year, 7, 5),
            "fixed": True,
            "public_other": "Public",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Den upálení mistra Jana Husa",
            "holiday_name_en": "Jan Hus Day",
            "date": date(year, 7, 6),
            "fixed": True,
            "public_other": "Public",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Den české státnosti",
            "holiday_name_en": "Czech Statehood Day",
            "date": date(year, 9, 28),
            "fixed": True,
            "public_other": "Public",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Den vzniku samostatného československého státu",
            "holiday_name_en": "Czechoslovak Independence State Day",
            "date": date(year, 10, 28),
            "fixed": True,
            "public_other": "Public",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Den boje za svobodu a demokracii a Mezinárodní den studentstva",
            "holiday_name_en": "Struggle for freedom and democracy and International Student Day",
            "date": date(year, 11, 17),
            "fixed": True,
            "public_other": "Public",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Štědrý den",
            "holiday_name_en": "Christmas Eve",
            "date": date(year, 12, 24),
            "fixed": True,
            "public_other": "Other",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "1. svátek vánoční",
            "holiday_name_en": "Christmas Day",
            "date": date(year, 12, 25),
            "fixed": True,
            "public_other": "Other",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "2. svátek vánoční",
            "holiday_name_en": "St. Stephen's Day",
            "date": date(year, 12, 26),
            "fixed": True,
            "public_other": "Other",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Velký pátek",
            "holiday_name_en": "St. Stephen's Day",
            "date": easter(year) + timedelta(days=-2),
            "fixed": False,
            "public_other": "Other",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Velikonoční pondělí",
            "holiday_name_en": "Easter Monday",
            "date": easter(year) + timedelta(days=1),
            "fixed": False,
            "public_other": "Other",
            "working_day": False,
            "description_en": "",
            "description_cz": ""
        },

    )

    return holidays


def get_working_days(year):
    holiday_dates = set(holiday["date"] for holiday in get_holidays(year))

    working_days = list()

    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)

    while start_date <= end_date:
        if start_date not in holiday_dates and start_date.strftime("%A") not in ("Sunday", "Saturday"):
            working_days.append(start_date)

        start_date += timedelta(days=1)

    return working_days
