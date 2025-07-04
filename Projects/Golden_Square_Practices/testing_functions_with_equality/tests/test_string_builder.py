from lib.string_builder import *

"""
add no string "" and check the size and the output. 
add("")
size() returns 0
output() returns ""
"""
def test_add_no_strings():
    stringbuilder = StringBuilder()
    size = stringbuilder.size()
    output = stringbuilder.output()
    assert size == 0
    assert output == ""

"""
add one string 'hello'
size() should retrun 5
output() should retrun "hello"
"""
def test_add_one_strings():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello")
    size = stringbuilder.size()
    output = stringbuilder.output()
    assert size == 5
    assert output == "hello"


"""
add two strings 'hello,' and ' world'
size() should return 12
output() should return "hello, world"
"""
def test_add_two_strings():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello, ")
    stringbuilder.add("world")

    size = stringbuilder.size()
    output = stringbuilder.output()
    assert size == 12
    assert output == "hello, world"

"""
add 3 strings 'hello,' and ' world. ' and 'How are you?'
size() should return 25
output() should return "hello, world. How are you?"
"""
def test_add_three_strings():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello, ")
    stringbuilder.add("world. ")
    stringbuilder.add('How are you?')
    size = stringbuilder.size()
    output = stringbuilder.output()
    assert size == 26
    assert output == "hello, world. How are you?"

"""
add an f"world, {5}" string and "hello "
size() should return 14
output() should return 'hello world, 5'
"""

def test_add_fstring_strings():
    stringbuilder = StringBuilder()
    stringbuilder.add("hello ")
    stringbuilder.add(f"world, {5}")
    size = stringbuilder.size()
    output = stringbuilder.output()
    assert size == 14
    assert output == "hello world, 5"