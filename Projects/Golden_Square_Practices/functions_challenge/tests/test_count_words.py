from lib.count_words import *
import lib.count_words
import pytest
"""
test to see if count_words() exist
should return true
"""
def test_if_count_words_exists():
    assert hasattr(lib.count_words, 'count_words')

"""
test to see if the count_words() function only takes a string input parameter
input a non-string data type and it should raise a typeerror "please give a string"
"""
def test_if_input_is_string():
    with pytest.raises(TypeError) as e:
            word_counter = count_words(789)
    error_message = str(e.value)
    assert error_message == 'Please give a string'

"""
test input a normal string with 5 words
should return 5
"""
def test_normal_string_of_5_words():
    word_counter = count_words("Hello, how are you today?")
    assert word_counter == 5

"""
test an empty string "" it should return "String is empty"
"""
def test_empty_string_without_space():
    word_counter = count_words("")
    assert word_counter == "String is empty"
"""
test an empty string with space " " should return "String is empty
"""
def test_empty_string_with_space():
    word_counter = count_words(" ")
    assert word_counter == "String is empty"
    