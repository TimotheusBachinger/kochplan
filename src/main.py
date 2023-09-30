import calendar
import datetime
from .mytypes import Month, WeekDay, Cookday, ThemesDays, Cooker
import holidays
from itertools import cycle


BAVARIAN_HOLIDAYS = holidays.DE(subdiv="BY", language="de")  # type: ignore


def build_plan(month: Month, year: int, cookers: list[str]) -> list[Cookday]:
    cookdays = days_to_cook(month, year)
    cookers_cylce = cycle(map(Cooker, cookers))

    return [
        Cookday(
            cooker=next(cookers_cylce), theme=ThemesDays[WeekDay(d.weekday())], day=d
        )
        for d in cookdays
    ]


def is_holiday(day: datetime.date) -> bool:
    """
    >>> is_holiday(datetime.date(2023,10,3))
    True
    >>> is_holiday(datetime.date(2023,10,4))
    False
    """
    return BAVARIAN_HOLIDAYS.get(day) is not None


def is_workingday(day: WeekDay) -> bool:
    """
    >>> is_workingday(WeekDay.Montag)
    True
    >>> is_workingday(WeekDay.Sonntag)
    False
    """
    return day not in (WeekDay.Samstag, WeekDay.Sonntag)


def days_of_month(month: Month, year: int) -> list[datetime.date]:
    return [
        d
        for w in calendar.Calendar().monthdatescalendar(year, month)
        for d in w
        if d.month == month
    ]


def days_to_cook(
    month: Month,
    year: int,
    exceptions: list[datetime.date] = [],
) -> list[datetime.date]:
    return [
        d
        for d in days_of_month(month, year)
        if is_workingday(WeekDay(d.weekday()))
        and not is_holiday(d)
        and d not in exceptions
    ]
