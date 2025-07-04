from lib.present import *
import pytest

"""
first try to wrap nothing
which should work then try to unrwap and it will rais an exception and say "No contents have been wrapped."
"""
def test_wrap_nothing():
    wrapper = Present()
    wrapper.wrap(None)
    with pytest.raises(Exception) as e:
        wrapper.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

    
"""
next wrap somthing and then then uwrapit to have itself returned 
"""
def test_wrap_something():
    wrapper = Present()
    wrapper.wrap("Happy Brithday")
    result = wrapper.unwrap()
    assert result == "Happy Brithday"


"""
after having wrapped somthing, try to wrap something again
this shouls rais an exception and return "A contents has already been wrapped."
"""
def test_wrap_something_twice():
    wrapper = Present()

    wrapper.wrap("Happy Brithday")

    with pytest.raises(Exception) as e:
        wrapper.wrap("Happy Anniversary")
    
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."