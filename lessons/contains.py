"""Example of writing a function to search a list"""

# Define a function named contains
#  Parameters:
#   1. needle - the str we're searching for
#   2. haystack - the list of str variables we're searching through
def contains(needle: str, haystack: list[str]) -> bool:
    """Test if needle is found in haystack"""
    for item in haystack:
        if item == needle:
            return True
    return False
#  Algorithm: for each item in haystack:
#       Test if equal to needle
#           If so, return true
#   After all items checked, that means needle not found, return False
# Returns True if needle is found in haystack
