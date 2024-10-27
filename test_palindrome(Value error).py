"""
Tests the palindrome module
"""
import pytest
from palindrome import is_palindrome

def test_is_palindrome():
    with pytest.raises(ValueError):
        is_palindrome(2)