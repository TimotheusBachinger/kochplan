from enum import IntEnum, StrEnum, auto
from dataclasses import dataclass
from typing import Mapping, Final, NewType
from datetime import date


class Month(IntEnum):
    Januar = auto()
    Februar = auto()
    März = auto()
    April = auto()
    Mai = auto()
    Juni = auto()
    Juli = auto()
    August = auto()
    September = auto()
    Oktober = auto()
    November = auto()
    Dezember = auto()


class WeekDay(IntEnum):
    Montag = 0
    Dienstag = 1
    Mittwoch = 2
    Donnerstag = 3
    Freitag = 4
    Samstag = 5
    Sonntag = 6


class Theme(StrEnum):
    Getreide = auto()
    Nudeln = auto()
    Reis = auto()
    Suppe = "Suppe & Nachtisch"
    Kartoffeln = auto()


ThemesDays: Mapping[WeekDay, Theme] = {
    WeekDay.Montag: Theme.Getreide,
    WeekDay.Dienstag: Theme.Nudeln,
    WeekDay.Mittwoch: Theme.Reis,
    WeekDay.Donnerstag: Theme.Suppe,
    WeekDay.Freitag: Theme.Kartoffeln,
}

Cooker = NewType("Cooker", str)


@dataclass
class Cookday:
    # TODO: Kiga Krippe or both
    day: date
    theme: Theme
    cooker: Cooker
