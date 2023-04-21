
from datetime import timedelta, date
from dateutil.easter import easter
from warnings import warn


def get_holidays(year: int,
                 dates_only: bool = False,
                 dates_and_cz_names: bool = False,
                 dates_and_en_names: bool = False,
                 shopping_restricted: bool = False):

    """
    This function generates holidays (public and other) when working is usually restricted according to labor Law.
    Also offers possibilities to filter dates only, czech or english names or shopping restricted days.

    :param year: Desired year to generate holidays (int)
    :param dates_only: Returns only dates -> [datetime.date(2023, 1, 1), ...]
    :param dates_and_cz_names: Returns only dates and cz names
            -> [[datetime.date(2023, 1, 1), 'Den obnovy samostatného českého státu'], ...]
    :param dates_and_en_names: Returns only dates and cz names
            -> [[datetime.date(2023, 1, 1), 'Restoration Day of the Independent Czech State'], ...]
    :param shopping_restricted: If true, filters out only holidays when shopping is restricted
            and can be combined with other parameters
    :return: If dates or names not selected individually, returns list with dictionaries including information
                about individual holidays
    """
    if year < 2001:
        raise Exception("Data are valid since year 2001")

    holidays = [
        # Except Good Friday and Easter Monday, all holidays has fixed date

        {
            "holiday_name_cz": "Den obnovy samostatného českého státu",
            "holiday_name_en": "Restoration Day of the Independent Czech State",
            "date": date(year, 1, 1),
            "fixed": True,
            "public_other": "Public",
            "valid_from": 2001,
            "shopping_restricted": True,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Nový Rok",
            "holiday_name_en": "New Year's Day",
            "date": date(year, 1, 1),
            "fixed": True,
            "public_other": "Other",
            "valid_from": 2001,
            "shopping_restricted": True,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Velký pátek",
            "holiday_name_en": "St. Stephen's Day",
            "date": easter(year) + timedelta(days=-2),
            "fixed": False,
            "public_other": "Other",
            "valid_from": 2016,
            "shopping_restricted": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Velikonoční pondělí",
            "holiday_name_en": "Easter Monday",
            "date": easter(year) + timedelta(days=1),
            "fixed": False,
            "public_other": "Other",
            "valid_from": 2001,
            "shopping_restricted": True,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Svátek práce",
            "holiday_name_en": "Labor Day",
            "date": date(year, 5, 1),
            "fixed": True,
            "public_other": "Other",
            "valid_from": 2001,
            "shopping_restricted": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Den vítězství",
            "holiday_name_en": "Victory Day",
            "date": date(year, 5, 8),
            "fixed": True,
            "public_other": "Public",
            "valid_from": 2001,
            "shopping_restricted": True,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Den slovanských věrozvěstů Cyrila a Metoděje",
            "holiday_name_en": "Saints Cyril and Methodius Day",
            "date": date(year, 7, 5),
            "fixed": True,
            "public_other": "Public",
            "valid_from": 2001,
            "shopping_restricted": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Den upálení mistra Jana Husa",
            "holiday_name_en": "Jan Hus Day",
            "date": date(year, 7, 6),
            "fixed": True,
            "public_other": "Public",
            "valid_from": 2001,
            "shopping_restricted": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Den české státnosti",
            "holiday_name_en": "Czech Statehood Day",
            "date": date(year, 9, 28),
            "fixed": True,
            "public_other": "Public",
            "valid_from": 2001,
            "shopping_restricted": True,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Den vzniku samostatného československého státu",
            "holiday_name_en": "Czechoslovak Independence State Day",
            "date": date(year, 10, 28),
            "fixed": True,
            "public_other": "Public",
            "valid_from": 2001,
            "shopping_restricted": True,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Den boje za svobodu a demokracii a Mezinárodní den studentstva",
            "holiday_name_en": "Struggle for freedom and democracy and International Student Day",
            "date": date(year, 11, 17),
            "fixed": True,
            "public_other": "Public",
            "valid_from": 2001,
            "shopping_restricted": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "Štědrý den",
            "holiday_name_en": "Christmas Eve",
            "date": date(year, 12, 24),
            "fixed": True,
            "public_other": "Other",
            "valid_from": 2001,
            "shopping_restricted": False,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "1. svátek vánoční",
            "holiday_name_en": "Christmas Day",
            "date": date(year, 12, 25),
            "fixed": True,
            "public_other": "Other",
            "valid_from": 2001,
            "shopping_restricted": True,
            "description_en": "",
            "description_cz": ""
        },

        {
            "holiday_name_cz": "2. svátek vánoční",
            "holiday_name_en": "St. Stephen's Day",
            "date": date(year, 12, 26),
            "fixed": True,
            "public_other": "Other",
            "valid_from": 2001,
            "shopping_restricted": True,
            "description_en": "",
            "description_cz": ""
        }
    ]

    if year < 2016:
        # Removes Good Friday from holidays as it was not applicable till 2016 (Zákon č. 359/2015 Sb.)
        holidays.pop(2)

    if shopping_restricted:
        if year < 2016:
            raise Exception("Shopping resctriction came into effect 01/10/2016 (DD/MM/YY)")
        elif year == 2016:
            # shopping restricted holidays before legslation change is filtered out
            holidays = list(filter(lambda x:
                                   x["shopping_restricted"] is True and x["date"] > date(2016, 10, 1), holidays))
            warn("Shopping resctriction came into effect 01/10/2016 (DD/MM/YY) thus holidays that are usually "
                 "shopping restricted are not filtered. This applies only for year 2016")
        else:
            holidays = list(filter(lambda x: x["shopping_restricted"] is True, holidays))

    if dates_only:
        holiday_dates = list(set(holiday["date"] for holiday in holidays))
        return holiday_dates

    if dates_and_cz_names:
        holiday_dates_cz_names = [[x["date"], x["holiday_name_cz"]] for x in holidays]
        return holiday_dates_cz_names

    if dates_and_en_names:
        holiday_dates_en_names = [[x["date"], x["holiday_name_en"]] for x in holidays]
        return holiday_dates_en_names

    return holidays


def get_workdays(year: int,
                 include_saturday: bool = False,
                 include_sunday: bool = False,
                 include_holidays: bool = False) -> list:

    """

    :param year: Desired year to generate holidays (int)
    :param include_saturday: Includes also Saturdays in output
    :param include_sunday: Includes also Sundays in output
    :param include_holidays: Counts holidays as working days
    :param shopping_days: Includes also shopping restricted days in output if not weekend.
            Can be combined with include_saturday/sunday parameter
    :return: List of all working days -> [datetime.date(2023, 1, 2), ...]
    """

    holiday_dates = set(holiday["date"] for holiday in get_holidays(year)) if not include_holidays else set()

    weekend_days = ["Saturday", "Sunday"]
    if include_saturday:
        weekend_days.remove("Saturday")

    if include_sunday:
        weekend_days.remove("Sunday")

    # while loop variables
    working_days = list()
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)

    while start_date <= end_date:
        if start_date not in holiday_dates and start_date.strftime("%A") not in weekend_days:
            working_days.append(start_date)

        start_date += timedelta(days=1)

    return working_days


def get_holidays_during_weekend(year: int) -> list:
    holiday_dates = list(holiday["date"] for holiday in get_holidays(year)
                        if holiday["date"].strftime("%A") in ("Saturday", "Sunday"))

    return holiday_dates

print(get_workdays(2023, include_holidays=True, include_sunday=True))