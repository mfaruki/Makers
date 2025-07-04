from lib.report_length import *

"""
if string 'Hello' is given
Returns 'This string was 5 characters long.'
"""
def test_with_string_hello():
    result = report_length('hello')
    assert result == 'This string was 5 characters long.'


"""
If string 'Goodbye, World!' is given
returns 'This string was 15 characters long.'
"""
def test_with_goodbye_string():
    result = report_length('Goodbye, World!')
    assert result == 'This string was 15 characters long.'




"""
If string data type is not given e.g. an integer is given
Returns None
"""
# def test_with_wrong_datatype_int():
#     result = report_length(786)
#     assert result == "TypeError: object of type 'int' has no len()"