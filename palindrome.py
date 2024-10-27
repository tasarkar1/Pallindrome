"""
Validates strings as palindromes.
"""
from collections import deque

def is_palindrome(x):
   d= deque(x)
   if type(x) is not str:
      raise ValueError
   while len(d) >1:
           if d.popleft() != d.pop():
             return False

   return True





print(is_palindrome("radar"))