# Czech Workdays, Holidays and Shopping Days
 This package includes Czech public and other holidays which are not working days, 
 working days calculator for selected year, the possibility to get public holidays that are during the weekend 
 and shopping days.

Working with holidays, you always have to select year. Additionally, you can choose to get only dates, dates with
English or Czech names of holidays or holidays that are working restricted.

Working with workdays, you always have to select year. Additionally, you can choose to include Saturday and Sunday
as workday and you can also include working restriced holidays as workdays. Combinations of these parameters
are possible.

Data are valid since 2001. If selected year before 2001, exception is raised.

#### Informational sources
[Czech holidays in English](https://en.wikipedia.org/wiki/Public_holidays_in_the_Czech_Republic)  
[Czech holidys in Czech](https://cs.wikipedia.org/wiki/%C4%8Cesk%C3%BD_st%C3%A1tn%C3%AD_sv%C3%A1tek)

#### Legislation sources
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

Calling function `get_holidays()` with argument `dates_only=True` will return unsorted list of `datetime.date(YYYY/MM//DD)` holidays

```Python
>>> from czech_workdays_holidays import get_holidays
>>> get_holidays(2023, dates_only=True)

[datetime.date(2023, 5, 1), datetime.date(2023, 4, 7), datetime.date(2023, 10, 28), datetime.date(2023, 12, 25), datetime.date(2023, 12, 26), datetime.date(2023, 4, 10), datetime.date(2023, 7, 5), datetime.date(2023, 11, 17), datetime.date(2023, 12, 24), datetime.date(2023, 5, 8), datetime.date(2023, 7, 6), datetime.date(2023, 9, 28), datetime.date(2023, 1, 1)]
```

### get_workdays()

This function calculates the number of workdays in a given year, taking into account optional parameters for including or excluding weekend days and holidays.

Raises exception if year entered is 2000 and earlier.

#### Example 1

Calling function `get_workdays()` with argument `include_ holidays=True` and with argument `include_sunday` will return sorted list of `datetime.date(YYYY/MM//DD)` workdays

Notice that 2023/1/1 was a Sunday and Holiday and it is in the output. If one of those arguments were False, it would not appear. 

```Python
>>> from czech_workdays_holidays import get_workdays
>>> get_workdays(2023, include_sunday=True, include_holidays=True)

[datetime.date(2023, 1, 1), datetime.date(2023, 1, 2), datetime.date(2023, 1, 3), ... , datetime.date(2023, 12, 31)]
```

#### Example 2