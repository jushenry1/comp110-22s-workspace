"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730411898"

from itertools import count


five_letter_word: str = input("Enter a five letter word: ")
if (len(five_letter_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()

single_character: str = input("Enter a single character: ")
if (len(single_character) != 1):
     print("Error: Character must be a single character.")
     exit()

print("Searching for " + single_character + " in " + five_letter_word)

count_instances_of_letter: int = 0
count_instances_of_letter = five_letter_word.count(single_character)
if (five_letter_word[0] == single_character):
    print(single_character + " found at index 0.")
if (five_letter_word[1] == single_character):
    print(single_character + " found at index 1.")
if (five_letter_word[2] == single_character):
    print(single_character + " found at index 2.")
if (five_letter_word[3] == single_character):
    print(single_character + " found at index 3.")
if (five_letter_word[4] == single_character):
    print(single_character + " found at index 4.")


if (count_instances_of_letter == 1):
    print("1 instance of " + single_character + " found in " + five_letter_word)
elif (count_instances_of_letter == 2):
    print("2 instances of " + single_character + " found in " + five_letter_word)
elif (count_instances_of_letter == 3):
    print("3 instances of " + single_character + " found in " + five_letter_word)
elif (count_instances_of_letter == 4):
    print("4 instances of " + single_character + " found in " + five_letter_word)
elif (count_instances_of_letter == 5):
    print("5 instances of " + single_character + " found in " + five_letter_word)
elif (count_instances_of_letter == 0):
    print ("No instances of " + single_character + " found in " + five_letter_word)