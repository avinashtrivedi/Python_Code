# parse.py
# Walker M. White (wmw2)
# September 1, 2014
"""Further functions for manipulating strings

This module contains two functions: replace_first and parse_sum.  It is 
kept separate from Lab 3 in order to cut down on the amount of time that 
it takes to complete Lab 3.

The functions in this module may include intentional errors."""


def replace_first(word,a,b):
    """Returns: a copy of word with the FIRST instance of a replaced by b
    
    Example: replace_first('crane','a','o') returns 'crone'
    Example: replace_first('poll','l','o') returns 'pool'
    
    Precondition: word, a, and b are strings.  a is a substring of word."""
    pos = word.rfind(a)
    before = word[:pos]
    after  = word[pos+1:]
    result = before+b+after
    return result


def parse_sum(s):
    """Returns: the value of the sum represented by string s
    
    This function is given a string with three numbers connected by
    an addition sign, such a '1.2+3.5+5.7'.  This function extracts
    the three values from the string using slicing, and then adds 
    them together.
    
    Example: parse_sum('1.5+2+3.2') returns 6.7
    
    Precondition: s is a string representing sum of three numbers"""
    # Find the first plus
    first = s.find("+")
    
    # First number ends before the plus sign
    string1 = s[:first]
    
    # Get the slice after the first plus sign
    after_plus = s[first:]
    
    # Use new slice to find the plus sign
    second = after_plus.find("+")
    
    # Use second plus to get the last two numbers
    # REMEMBER: Working with after_plus, not s!!
    string2 = after_plus[0:second]
    string3 = after_plus[second+1:]

    # Convert the strings to numbers
    x = float(string1)
    y = float(string2)
    z = float(string3)

    # Add them together
    return x+y+z