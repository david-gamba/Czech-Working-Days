# Czech Workdays, Holidays and Shopping Days
 This package includes Czech public and other holidays which are not working days, 
 working days calculator for selected year, the possibility to get public holidays that are during the weekend 
 and shopping days.

Working with holidays, you always have to select year. Additionally, you can choose to get only dates, dates with
English or Czech names of holidays or holidays that are working restricted.

Working with workdays, you always have to select year. Additionally, you can choose to include Saturday and Sunday
as workday. Combinations of these parameters
are possible.

Working with workdays, you always have to select year.Additionally, you can choose to exclude Saturdays and Sundays 
and/or include shopping restricted days.

Data are valid since 2001. If selected year before 2001, exception is raised.

#### Informational sources
[Czech holidays in English](https://en.wikipedia.org/wiki/Public_holidays_in_the_Czech_Republic)  
[Czech holidys in Czech](https://cs.wikipedia.org/wiki/%C4%8Cesk%C3%BD_st%C3%A1tn%C3%AD_sv%C3%A1tek)

#### Legal sources
[Czech Holidays](https://www.zakonyprolidi.cz/cs/2000-245?text=245%2F2000)  
[Restricted shopping days](https://www.zakonyprolidi.cz/cs/2016-223)

## Installation
`pip install czech-workdays-holidays`

## Import
`import czech_workdays_holidays`

## Functions

### get_holidays()
This function generates holidays (public and other) when working is usually restricted according to labor law. It offers options to filter dates only, Czech or English names, and shopping-restricted days.

Raises exception if year entered is 2000 and earlier.
#### Example

Calling function `get_holidays()` with argument `dates_only=True` will return unsorted list

```Python
>>> from czech_workdays_holidays import get_holidays
>>> get_holidays(2023, dates_only=True)

[datetime.date(2023, 5, 1), datetime.date(2023, 4, 7), datetime.date(2023, 10, 28), datetime.date(2023, 12, 25), datetime.date(2023, 12, 26), datetime.date(2023, 4, 10), datetime.date(2023, 7, 5), datetime.date(2023, 11, 17), datetime.date(2023, 12, 24), datetime.date(2023, 5, 8), datetime.date(2023, 7, 6), datetime.date(2023, 9, 28), datetime.date(2023, 1, 1)]
```

### get_workdays()

This function calculates the number of workdays in a given year, taking into account optional parameters for including or excluding weekend days and holidays

By default, function return workdays in a given year. If parameters are set to False, it will return Monday to Friday days.

In case you set `include_saturday=True`, it will return Monday to Saturday days but Saturdays that are also holidays would be excluded.  
In case you set `include_holidays=True` and including weekend days would remain False then holidays during weekend would not be returned.

Raises exception if year entered is 2000 and earlier

#### Example

Calling function `get_workdays()` with argument `include_holidays=True` and with argument `include_sunday` will return sorted list of `datetime.date(YYYY/MM//DD)` workdays

Notice that 2023/1/1 was a Sunday and Holiday and it is in the output. If one of those arguments were False, it would not appear

```Python
>>> from czech_workdays_holidays import get_workdays
>>> get_workdays(2023, include_sunday=True, include_holidays=True)

[datetime.date(2023, 1, 1), datetime.date(2023, 1, 2), datetime.date(2023, 1, 3), ... , datetime.date(2023, 12, 31)]
```

### get_shopping_days()

Gets all shopping days in a given year. Full year returned if all parameters are True. Possibility to combine
parameters

In the output, 2023/1/1 is excluded as it is Sunday and shopping restricted day then 2023/30/12 is included
as it is Saturday which has set default value to true: `include_saturday=True`. Then 2023/31/12 is excluded 
as it is Sunday.

Raises exception if year entered is 2000 and earlier.

#### Example

```Python
>>> from czech_workdays_holidays import get_shopping_days
>>> get_shopping_days(2023, include_sunday=False, exclude_shopping_restricted_days=False)

[datetime.date(2023, 1, 2), datetime.date(2023, 1, 3), ... , datetime.date(2023, 12, 29), datetime.date(2023, 12, 30)]
```

### get_holidays_during_weekend()

Returns all holidays in given year that are during weekend

Raises exception if year entered is 2000 and earlier.

#### Example

```Python
>>> from czech_workdays_holidays import get_holidays_during_weekend
>>> get_holidays_during_weekend(2023)

[datetime.date(2023, 1, 1), datetime.date(2023, 10, 28), datetime.date(2023, 12, 24)]
```

### get_workdays_during_weekend()

Returns all workdays in given year that are during weekend with possibility to exclude Sunday/Saturday
and include holidays. If weekend parameters set to True and `include_holidays=False` the function would
not return workdays that are during weekend and are holidays.

Raises exception if year entered is 2000 and earlier.

In example below, 1/1/2023 and 24/12/2023 are excluded as it is Sunday and holiday.

#### Example

```Python
>>> from czech_workdays_holidays import get_workdays_during_weekend
>>> get_workdays_during_weekend(2023)

[datetime.date(2023, 1, 7), datetime.date(2023, 1, 8), datetime.date(2023, 1, 14), ... , datetime.date(2023, 12, 23), datetime.date(2023, 12, 30), datetime.date(2023, 12, 31)]
```