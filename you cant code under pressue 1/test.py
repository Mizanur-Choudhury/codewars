from main import *


def test_1():
    assert double_integer(4) == 8


def test_2():
    assert double_integer(2) == 4


def test_3():
    assert double_integer(3) == 6


def test_4():
    assert double_integer(789) == 1578
