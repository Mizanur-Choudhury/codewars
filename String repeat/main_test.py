from main import *
from string_multiplier_user import *


def test_multiple_string():
    assert multiple_string(4, "Hi") == ("HiHiHiHi")


def test_multiple_string_spaces():
    assert multiple_string(4, "Sup ") == ("Sup Sup Sup Sup ")


def test_multiple_string_number_2():
    assert multiple_string(2, "Cupcake") == ("CupcakeCupcake")


def test_leading_spaces():
    assert multiple_string(2, " sup") == (" sup sup")


def test_user_input():
    assert user_input_number(22) == 22
