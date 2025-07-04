from lib.high_value import *

"""
inpjut 1 and 2 and see if get_highest works
should return second value is higher
"""

def test_second_value_higher():
    valuer = HighValue(1,2)
    result = valuer.get_highest()
    assert result == "Second value is higher"

"""
input 2 and 1 and see igf get_highest wors
should return first value is higher
"""
def test_first_value_higher():
    valuer = HighValue(2,1)
    result = valuer.get_highest()
    assert result == "First value is higher"
"""
input two of the same values
get_highest should reurn values are equal
"""
def test_input_equal_values():
    valuer = HighValue(2,2)
    result = valuer.get_highest()
    assert result == "Values are equal"

"""
check to see if add() actually increases by the value given for the first value
"""
def test_increase_second_value():
    valuer = HighValue(2,1)
    valuer.add(4,'second')
    result = valuer.get_highest()
    assert result == "Second value is higher"

"""
check to see if add() actually increases by the value given for the second value
"""
def test_increase_first_value():
    valuer = HighValue(1,2)
    valuer.add(4,'first')
    result = valuer.get_highest()
    assert result == "First value is higher"

def test_floating_point_value():
    valuer = HighValue(1.3,2.8)
    result = valuer.get_highest()
    assert result == "Second value is higher"

def test_char_input():
    valuer = HighValue('a','b')
    result = valuer.get_highest()
    assert result == "Second value is higher"

def test_string_input():
    valuer = HighValue('hello','goodbye')
    result = valuer.get_highest()
    assert result == "First value is higher"

def test_list_input():
    valuer = HighValue([1,2,3,4], [5,6,7,8])
    result = valuer.get_highest()
    assert result == "Second value is higher"