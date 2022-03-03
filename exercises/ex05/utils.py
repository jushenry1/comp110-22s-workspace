"""Ex05 utils.py"""

__author__ = "730411898"

from utils import only_evens
from utils import sub
from utils import concat

def only_evens(a: list[int]) -> list[int]:
    """Gives us only even numbers"""
    even_numbers: list[int] = []
    for x in a:
        if x % 2 == 0:
            even_numbers.append(x)
    return even_numbers

def sub(b: list[int], begin: int, climax: int) -> list[int]:
    """Gives a subset of list"""
    subset: list[int] = []
    if len(b) <= 0 or begin > len(b) or climax <= 0 or begin > climax - 1:
        return subset
    if begin < 0:
        begin = 0
    if climax > len(b):
        climax = len(b)
    s: int = begin 
    while s < len(b):
        if s < climax:
            subset.append(b[s])
        s = s + 1
    return subset

def concat(c: list[int], d: list[int]) -> list[int]:
    """Concatting two list"""
    list_0: list[int] = []
    for x in c:
        list_0.append(x)
    for y in d:
        list_0.append(y)
    return list_0





