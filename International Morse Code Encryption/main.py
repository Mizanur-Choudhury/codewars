"""
Write a function that will encrypt a given sentence into International Morse Code, both the input and out puts will be strings.
Characters should be separated by a single space. Words should be separated by a triple space.
"""
from morse_code_dict import *


def encryption(text: str) -> str:
    morse_alphabet = morse_code
    morse_sentence = []
    for char in text:
        """
        im using sentence, as i made my own morse code dictionary, to account for upper and lowercase, however you
        can use upper.sentence instead to shift the input text to upper
        """
        if char != ' ':  # get the string character is not a empty string then get the morse code character
            morse_char = morse_code.get(char)
            # get method The get() method returns the value of the item with the specified key
            if morse_char:
                morse_sentence.append(morse_char)  # if we get a character, append to empty list
        else:
            morse_sentence.append(' ')  # if no character add a space

    return ' '.join(morse_sentence)

