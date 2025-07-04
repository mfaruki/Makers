from lib.greet import *

def test_greet_with_a_name():
    result = greet('John')
    assert result == 'Hello, John!'