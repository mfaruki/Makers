from lib.diary import *
import lib.diary
import pytest

"""
test to see if make_snippet functoin exists
"""
def test_if_make_snippet_exists():
    assert hasattr(lib.diary,'make_snippet')


"""
test to see if the input given in the function is a string
"""
def test_if_function_takes_string_input():
    with pytest.raises(TypeError) as e:
        make_snippet(5)
    error_message = str(e.value)
    assert error_message == "Parameter 'input_string' must be type String"

"""
test to see if a string is less than 5 words
should return the string
"""
def test_if_input_string_is_less_than_5():
    result = make_snippet("Hello how are you")
    assert result == "Hello how are you"


"""
test to see if a string is 5 words
should return the string
"""
def test_if_input_string_is_5():
    result = make_snippet("Hello, how are you today?")
    assert result == "Hello, how are you today?"

"""
test to see if a string is more than 5 words
should return the first five words + '...'
"""
def test_if_input_string_is_more_than_5():
    result = make_snippet("Hello, how are you today? Can I get you some juice?")
    assert result == "Hello, how are you today?..."

"""
test an empty string to see what it returns. 
shoud just return an empty string but i want my program to say "snippet is empty" 
"""
def test_if_snippet_is_empty():
    result = make_snippet("")
    assert result == "Snippet is empty"

"""
test an empty string but with a space " " to see what it returns. 
shoud just return an empty string but i want my program to say "snippet is empty" 
"""
def test_if_snippet_is_empty_with_space():
    result = make_snippet(" ")
    assert result == "Snippet is empty"