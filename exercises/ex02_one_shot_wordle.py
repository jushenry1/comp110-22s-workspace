"""EX02 - One-Shot Wordle - Loops!"""

__author__ = "730411898"

secret_word: str = "python" #This is the secret word the people playing are trying to guess.
six_letter_word: str = input("What is your 6-letter guess?") #This input will let the player guess a six letter word.
white_box: str = "\U00002B1C" #This is the variable to check and scratch out characters in six_letter_word.
green_box: str = "\U0001F7E9" #This is the variable to check and confirm that the character in six_letter_word is correct and in the right place.
yellow_box: str = "\U0001F7E8" #This is the variable to check and say that the character in six_letter_word is in the wrong place.
emoji: str = ""
index: int = 0
incorrect_placement: bool = False
index_two: int = 0

while (len(six_letter_word) != 6):
    six_letter_word= input("That was not 6 letters! Try again:") #This is a while loop incentivized for players to try again if they do not input six letters.
while (len(six_letter_word) == 6): #This line was made if the word does equal 6 letter.
    while(index < 6):
        if (six_letter_word[index] == secret_word[index]):
            emoji = emoji + green_box
            index = index + 1     
        else: 
            while(index_two < 6):
                if (six_letter_word[index] == secret_word[index_two]):
                    emoji = emoji + yellow_box
                    index_two = index_two + 1
                else:
                    index_two = index_two + 1
            if (six_letter_word[index] != "p", "y", "t", "h", "o", "n"):
                emoji = emoji + white_box
    if (six_letter_word == secret_word): #This line means if their six_letter_word is the same as the secret_word, they win and the program stops.
        print(emoji)
        print("Woo! You got it!")
        exit()
    if (six_letter_word != secret_word): #This line means if their six_letter_word isn't the same as the secret_word, they lose and the program stops.
        print(emoji)
        print("Not quite. Play again soon!")
        exit()                
    
    
    
    
    