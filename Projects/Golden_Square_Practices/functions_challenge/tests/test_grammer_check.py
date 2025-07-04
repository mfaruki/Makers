import lib.grammer_check

from lib.grammer_check import *

import pytest

def test_if_grammer_check_exists():
    assert hasattr(lib.grammer_check, 'grammer_check')

def test_if_input_is_string():
    with pytest.raises(TypeError) as e:
        grammer_check(5)
    error_message = str(e.value)
    assert error_message == "Please input a string"

def test_no_capital_but_ending_punctuation():
    tester = grammer_check("hello, how are you today?")
    assert tester == False

