"""
Validates strings as palindromes.
"""

from collections import deque
def is_palindrome(x):
    if type(x) is not str:
        raise ValueError
    if x == "":
        return False
    d= deque(str.lower(x))
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False


    return True

print(is_palindrome("Able was I ere I saw Elba"))