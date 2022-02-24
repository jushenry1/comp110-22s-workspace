"""EX03 - Structured Wordle!"""

__author__ = "730411898"


white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"


def contains_char(string_of_any_length: str, single_character_search: str) -> bool:
    """Searches if one letter is present in the word and prints True if found."""
    assert len(single_character_search) == 1
    if single_character_search in string_of_any_length:
        return(True)
    else: 
        return(False)


def emojified(guess: str, secret: str) -> str:
    """This looks emojified."""
    assert len(guess) == len(secret)
    emoji: str = ""
    index: int = 0
    while (index < len(secret)):
        if contains_char(secret[index], guess[index]) is True:
            emoji = emoji + green_box
            index = index + 1
        elif contains_char(secret, guess[index]) is True:
            emoji = emoji + yellow_box
            index = index + 1
        elif contains_char(secret, guess[index]) is False:
            emoji = emoji + white_box
            index = index + 1
    return(emoji)


def input_guess(word_length: int) -> str:
    """Checks the input length."""
    guess_word: str = input(f"Enter a {word_length} character word:")
    while len(guess_word) != word_length:
        guess_word = input(f"That wasn't {word_length} chars! Try again:")
    return guess_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
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