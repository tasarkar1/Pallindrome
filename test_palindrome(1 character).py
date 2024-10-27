"""
Tests the palindrome module
"""
import pytest
from palindrome import is_palindrome

def test_is_palindrome():
    assert is_palindrome("a") == True