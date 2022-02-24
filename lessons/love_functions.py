"""Some examples of tender, loving function definitions"""

from tkinter import Variable


def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}!"

def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    counter_variable = 0
    while counter_variable < n:
        love_note += love(to) + "/n"
        counter_variable += 1
    return love_note

def mystery(n: int) -> str:
    """A useless function."""
    i: int = 0
    while i < n:
        if i % 2 == 1: #integer division
            return "ooh"
        i += 1
        return "ahh" #this expression can never make ahh.
# return value is ooh, and vs return 
#     what returned when the following function definition is called with mystery:
#     "ahh"
# def mystery(n: int )