# lab03.py
# Walker M. White (wmw2)
# September 1, 2014
"""Functions for handling Strings

This module provides a few functions for manipulating strings.
This module is intended to prepare you for the first assignment.
The functions included here may include intentional errors."""

def has_a_vowel(s):
    """Returns: True if s has at least one vowel (a, e, i, o, or u)
    
    Precondition: s is a non-empty string"""
    return 'a' in s and 'e' in s and 'i' in s and 'o' in s and 'u' in s


def first_inside_quotes(s):
    """Returns: The first substring of s between two (double) quote characters
    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C'
    because it only picks the first such substring.
    
    Precondition: s is a string with at least two (double) quote characters inside"""
    start = s.find('"') + 1
    end = start + s[start+1:].find('"') + 1
    inner = s[start:end]
    
    return inner