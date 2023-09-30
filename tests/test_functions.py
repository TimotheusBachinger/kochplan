from src.main import days_of_month, days_to_cook, Month, build_plan
from datetime import date

from src.mytypes import Cookday, Theme


def test_build_plan():
    cookers = ["Joni", "Benno", "Timi"]
    plan = build_plan(Month.Oktober, 2023, cookers)
    assert plan[0:4] == [
        Cookday(
            day=date(2023, 10, 2),
            theme=Theme.Getreide,
            cooker="Joni",
        ),
        Cookday(
            day=date(2023, 10, 4),
            theme=Theme.Reis,
            cooker="Benno",
        ),
        Cookday(
            day=date(2023, 10, 5),
            theme=Theme.Suppe,
            cooker="Timi",
        ),
        Cookday(
            day=date(2023, 10, 6),
            theme=Theme.Kartoffeln,
            cooker="Joni",
        ),
    ]


def test_days_to_cook():
    days = days_to_cook(
        10,
        2023,
        exceptions=[date(2023, 10, 11)],
    )
    assert days == [
        date(2023, 10, 2),
        date(2023, 10, 4),
        date(2023, 10, 5),
        date(2023, 10, 6),
        date(2023, 10, 9),
        date(2023, 10, 10),
        date(2023, 10, 12),
        date(2023, 10, 13),
        date(2023, 10, 16),
        date(2023, 10, 17),
        date(2023, 10, 18),
        date(2023, 10, 19),
        date(2023, 10, 20),
        date(2023, 10, 23),
        date(2023, 10, 24),
        date(2023, 10, 25),
        date(2023, 10, 26),
        date(2023, 10, 27),
        date(2023, 10, 30),
        date(2023, 10, 31),
    ]


def test_days_of_month():
    days = days_of_month(Month.September, 2023)
    assert days == [
        date(2023, 9, 1),
        date(2023, 9, 2),
        date(2023, 9, 3),
        date(2023, 9, 4),
        date(2023, 9, 5),
        date(2023, 9, 6),
        date(2023, 9, 7),
        date(2023, 9, 8),
        date(2023, 9, 9),
        date(2023, 9, 10),
        date(2023, 9, 11),
        date(2023, 9, 12),
        date(2023, 9, 13),
        date(2023, 9, 14),
        date(2023, 9, 15),
        date(2023, 9, 16),
        date(2023, 9, 17),
        date(2023, 9, 18),
        date(2023, 9, 19),
        date(2023, 9, 20),
        date(2023, 9, 21),
        date(2023, 9, 22),
        date(2023, 9, 23),
        date(2023, 9, 24),
        date(2023, 9, 25),
        date(2023, 9, 26),
        date(2023, 9, 27),
        date(2023, 9, 28),
        date(2023, 9, 29),
        date(2023, 9, 30),
    ]
