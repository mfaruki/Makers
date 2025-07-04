# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._
    
```python
# EXAMPLE

def grammer_check(text):
    """checks to see if the text starts with a ciptal letter and ends with a suitable sentenc ending punctuation - '.' ',' '?' '!'

    Parameters: (list all parameters and their types)
        text: a long string containing words like a sentence. 

    Returns: (state the return value and its type)
       a boolean True if the input is grammitcally correct or False if not grammatically incorrect

    Side effects: (state any side effects)
        Prints True or False on the screen. 
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
test to see if the grammer_check() function exists
"""

"""
test to see if the function takes a string data type for 'text'
if input any other data type then should raise a typeerror message saying "Please input a string"
"""

"""
test to see if a text is given with out a starting capital letter but with a correct ending punctuation
"""

"""
test to see if a text is given with out a ending punctuation but with a starting capital letter
"""

"""
test to see if no capital letter or ending punctuation is given. 
"""

"""
test to see if both a starting capital letter and ending punctuation is correct 
"""

"""
test to see if string is empty. 
"""
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
