
def count_words(text):

    if not isinstance(text, str):
        raise TypeError('Please give a string')
    if text.strip() == "":
        return "String is empty"

    number_of_words = len(text.split())
    return number_of_words
    