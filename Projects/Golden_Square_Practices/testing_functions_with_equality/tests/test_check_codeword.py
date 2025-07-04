from lib.check_codeword import *
"""
If the code word is correct
Returns 'Correct! Come in.'
"""
def test_with_codeword_horse():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

"""
If the code word is close, and has the right first and last letter
Returns 'Close, but nope.'
"""
def test_codeword_that_is_close():
    result = check_codeword('house')
    assert result == "Close, but nope."


"""
if the codeword is wrong
returns 'WRONG!'
"""
def test_wrong_codeword():
    result = check_codeword('donkey')
    assert result == "WRONG!"


"""
test to see if the codeword function is case sensitve
input the right codeword but with a capital H 
should return 'WRONG!'
"""
def test_if_codeword_is_case_sensitve():
    result =check_codeword('Horse')
    assert result == "WRONG!"

"""
if the codeword starts with 'h' but does not end with 'e'
returns 'WRONG!'
"""
def test_with_wrong_start_close_codeword():
    result = check_codeword('hat')
    assert result == "WRONG!"

"""
if the codeword does not starts with 'h' but does end with 'e'
returns 'WRONG!'
"""
def test_with_wrong_end_close_codeword():
    result = check_codeword('mouse')
    assert result == "WRONG!"