# test_lab03.py
# <YOUR NAME HERE>
# <DATE HERE>
"""Unit test to test the module lab03.py"""

import cornelltest      # For assert_equals and assert_true
import lab03            # This is what we are testing
import parse            # (Optional part of the lab)


def test_first_inside_quotes():
    print('Testing function first_inside_quotes()')
    
    s='The instructions say "Dry-clean only".'
    result = lab03.first_inside_quotes(s)
    cornelltest.assert_equals('Dry-clean only',result)
    
    s='A "B C" D "E F" G'
    result = lab03.first_inside_quotes(s)
    cornelltest.assert_equals('B C',result)
    
    s='"The" instructions say Dry-clean only.'
    result = lab03.first_inside_quotes(s)
    cornelltest.assert_equals('The',result)
    
    s='"The" "instructions" "say" "Dry-clean only".'
    result = lab03.first_inside_quotes(s)
    cornelltest.assert_equals('The',result)
    
if __name__ == '__main__':
    test_first_inside_quotes()
    print('Module lab03 is working correctly')