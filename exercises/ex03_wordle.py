"""EX03 - Structured Wordle!"""

__author__ = "730411898"

from platform import java_ver
from re import X

white_box: str = "\U00002B1C" #This is the variable to check and scratch out characters in six_letter_word.
green_box: str = "\U0001F7E9" #This is the variable to check and confirm that the character in six_letter_word is correct and in the right place.
yellow_box: str = "\U0001F7E8" #This is the variable to check and say that the character in six_letter_word is in the wrong place.


def contains_char(string_of_any_length: str, single_character_search: str) -> bool:
    '''Searches if one letter is present 
    in the word and prints True if found.'''
    assert len(single_character_search) == 1
    if single_character_search in string_of_any_length:
        return(True)
    else: 
        return(False)


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret) #why do we use assert and not if here?
    emoji: str = ""
    index: int = 0
    while (index < len(secret)):
        if contains_char(secret[index], guess[index]) == True:
            emoji = emoji + green_box
            index = index + 1
        elif contains_char(secret, guess[index]) == True:
            emoji = emoji + yellow_box
            index = index + 1
        elif contains_char(secret, guess[index]) == False:
            emoji = emoji + white_box
            index = index + 1
    return(emoji)


def input_guess(word_length: int) -> str:
    guess_word: str = input(f"Enter a {word_length} character word:")
    while len(guess_word) != word_length:
        guess_word = input(f"That wasn't {word_length} chars! Try again:")
    return guess_word


def main() -> None:
    '''The entrypoint of the program and main game loop'''
    N: int = 1
    secret: str = "codes"
    guess: str = ""
    while N <= 6 and guess != secret:
        print(f"=== Turn {N}/6 ==")
        guess = input_guess(5)
        print(emojified(guess, secret))
        if(guess == secret):
            print(f"You won in {N}/6!")
        N += 1
    if N == 7:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()