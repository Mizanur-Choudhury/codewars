from main import *


def test_morse_code():
    assert encryption("hi mom") == ".... ..   -- --- --"  # "hi mom" test


def test_morse_code_upper():
    assert encryption("Hi mOM") == ".... ..   -- --- --"


def test_morse_numbers():
    assert encryption("0123") == "----- .---- ..--- ...--"


def test_more_letters():
    assert encryption("Show") == "... .... --- .--"
    assert encryption("the") == "- .... ."
    assert encryption("flare") == "..-. .-.. .- .-. ."
    assert encryption("star") == "... - .- .-."


def test_code_wars():
    assert encryption("HELLO WORLD") == ".... . .-.. .-.. ---   .-- --- .-. .-.. -.."
