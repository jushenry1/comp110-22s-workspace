"""EX06 Dictionary Test"""

__author__ = "730411898"

def contains(x: str, y: list[str]) -> bool:
    """We use this function to assist the invert function"""
    for item in y:
        if item == x:
            return True
    return False

def invert(a: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a dictionary"""
    result: dict[str, str] = dict()
    values_in_a: list[str] =list()
    for key in a:
        if contains(a[key], values_in_a): 
            raise KeyError("The same key was used.")
        result[a[key]] = key
        values_in_a.append(a[key])
    return result
        
def favorite_color(b: dict[str, str]) -> str:
    favorite: dict[str, int] = dict()
    color: list[str] = list()
    for key in b:
        if not contains(b[key], color):
            favorite[b[key]] = 1
            color.append(b[key])
        else:
            favorite[b[key]]= favorite[b[key]] + 1
    highest: int = 0
    for key in favorite:
        if favorite[key] > highest:
            highest = favorite[key]
    for key in favorite:
        if favorite[key] == highest:
            return key
    return"""Try again."""


def count(c: list[str]) -> dict[str, int]:
    """This is the count function"""
    dict_values_of_result: dict[str, int] = dict()
    list_values_of_result: list[str] = list()
    for x in c:
        if not contains(x, list_values_of_result):
            dict_values_of_result[x] =1
            list_values_of_result.append(x)
        else:
            dict_values_of_result[x] = dict_values_of_result[x] + 1
    return dict_values_of_result
    
        # d[key] = justin = key



    # invert_dict: dict[str, str]
    # invert_dict = dict()
    # invert_dict["John"] = "Emma"

    # #Declaring the type of a dictionary
    # schools: dict[str, int]
    # #initialize to an empty dictionary
    # schools = dict()
    # #set a key value paining in the dictionary
    # schools["UNC"] = 19400

    # print(schools)
    
    # schools: dict [str, str]
    # student = {'name': 'John'}
    # a= str
    # b= str
    # return({b,a})
    

