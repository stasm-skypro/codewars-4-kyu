"""This is the simple version of Fastest Code : Equal to 24.
Task
A game I played when I was young: Draw 4 cards from playing cards, use + - * /
and () to make the final results equal to 24. You will coding in function
equal_to_24. Function accept 4 parameters a b c d(4 cards), value range is 1-13.
The result is a string such as "2*2*2*3" ,(4+2)*(5-1); If it is not possible to
calculate the 24, please return "It's not possible!"
All four cards are to be used, only use three or two cards are incorrect; Use a
card twice or more is incorrect too. You just need to return one correct
solution, don't need to find out all the possibilities.
Examples
equal_to_24(1,2,3,4) // can return "(1+3)*(2+4)" or "1*2*3*4"
equal_to_24(2,3,4,5) // can return "(5+3-2)*4" or "(3+4+5)*2"
equal_to_24(3,4,5,6) // can return "(3-4+5)*6"
equal_to_24(1,1,1,1) // should return "It's not possible!"
equal_to_24(13,13,13,13) // should return "It's not possible!"
"""

from itertools import permutations


def equal_to_24(a, b, c, d):
    iterable = (a, b, c, d)
    perms = list(permutations(iterable, 4))
    print(perms)

    return "It's not possible!"


print(equal_to_24(1, 2, 3, 4) in ["(1+3)*(2+4)", "1*2*3*4"])
# print(equal_to_24(2, 3, 4, 5) in ["(5+3-2)*4", "(3+4+5)*2"])
# print(equal_to_24(3, 4, 5, 6) == "(3-4+5)*6")
# print(equal_to_24(1, 1, 1, 1) == "It's not possible!")
# print(equal_to_24(13, 13, 13, 13) == "It's not possible!")
