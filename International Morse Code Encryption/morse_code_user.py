"""
This is where the user, can input data to return the morse code value
"""

from main import encryption


def userinput(text: str) -> str:
    sentence = input("Write something here so i can translate it to morse code! ")
    return sentence


if __name__ == "__main__":
    (print(encryption(userinput(""))))
