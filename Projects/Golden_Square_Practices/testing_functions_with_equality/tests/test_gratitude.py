from lib.gratitudes import *

"""
test to see if gratitudes is initialised
shoudl return an empty string
"""
def test_empty_string():
    gratitude = Gratitudes()
    result = gratitude.format()
    assert result == "Be grateful for: "

"""
use the add method to append a gratitude 
then a format method to retrun the appended string
"""
def test_single_string_added():
    gratitude = Gratitudes()
    gratitude.add("Family")
    result = gratitude.format()
    assert result == "Be grateful for: Family"
"""
initialise the class, then try to return the formatted string with out appending a string. 
"""

"""
try to add an integer to the list
then see if the formatted string appends the integer to the string
"""

"""
try to add an f"" string to the list. 
"""