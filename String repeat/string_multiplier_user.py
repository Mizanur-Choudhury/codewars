from main import multiple_string
import string


def user_input_number(number: int) -> int:
    while True:
        try:
            number = int(input("Input your desired multiplier: "))
            # we want the user to input a number, this will keep looping until the user has input a correct integer
            break
        except ValueError:
            print("This is not a number! Try again!")
    return number


def user_input_string(text: str) -> str:
    while True:
        try:
            text = input("Input a single word: ")  # we want the user to input a string, so we spin up a while loop here

            if any(char in string.punctuation for char in text):

                break
        except ValueError:
            print("Text contains punctuation marks. Please remove it!")

    while True:
        try:
            if text.isalpha():  # We use this to check if the word is in the alphabet
                break  # break if this is true, end the loop
            else:
                print("That doesnt look like a single word to me!")
        except ValueError:
            print("Something went wrong!!!")
    return text
    # We are now returning the users inputs and multiplying them, using our main function!


if __name__ == "__main__":
    (print(multiple_string(user_input_string(user_input_number))))  # These are placeholders

