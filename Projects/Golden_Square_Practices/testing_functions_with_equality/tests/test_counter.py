from lib.counter import *

"""
if number 5 is addd only once
Returns "Counted to 5 so far."
"""
def test_add_one_number():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

"""
if number 5 is addd 5 times
Returns "Counted to 25 so far."
"""
def test_add_one_number_five_time():
    counter = Counter()
    counter.add(5)
    counter.add(5)
    counter.add(5)
    counter.add(5)
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 25 so far."

"""
if no number is added
Returns "Counted to 0 so far."
"""
def test_add_no_number():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

"""
if number 5, 6, then 7 is added
Returns "Counted to 18 so far."
"""
def test_add_three_different_number():
    counter = Counter()
    counter.add(5)
    counter.add(6)
    counter.add(7)
    result = counter.report()
    assert result == "Counted to 18 so far."

"""
if decimal number 78.8888, then 91.4444 is added
Returns "Counted to 170.3332 so far."
"""
def test_add_decimal_number():
    counter = Counter()
    counter.add(78.8888)
    counter.add(91.4444)
    result = counter.report()
    assert result == "Counted to 170.3332 so far."

"""
if negative number -67, then -23 is added
Returns "Counted to -90 so far."
"""
def test_add_negative_number():
    counter = Counter()
    counter.add(-67)
    counter.add(-23)
    result = counter.report()
    assert result == "Counted to -90 so far."

"""
if a formula or equation of 45*3 is given in the input and added 
returns "Counted to 135 so far."
"""
def test_add_multiplied_number():
    counter = Counter()
    counter.add(45*3)
    result = counter.report()
    assert result == "Counted to 135 so far."