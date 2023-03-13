"""
Write a function that accepts an integer n and a string s as parameters,
and returns a string of s repeated exactly n times.
"""


def multiple_string(number: int, text: str) -> (int, str):
    return number * text
    # arguments are passed by the user, and * multiples the text by the given amount
