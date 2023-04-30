from main import *


def test_logic():
    assert is_period_late(
        date(2023, 3, 24),
        date(2023, 4, 30),
        28
    ) == True


def test_logic_1():
    assert is_period_late(
        date(2023, 2, 24),
        date(2023, 4, 30),
        28
    ) == True


def test_logic_2():
    assert is_period_late(
        date(2023, 4, 29),
        date(2023, 4, 30),
        28
    ) == False


def test_logic_3():
    assert is_period_late(
        date(2023, 4, 10),
        date(2023, 4, 30),
        28
    ) == False
