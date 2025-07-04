def grammer_check(text):
    if not isinstance(text, str):
        raise TypeError("Please input a string")
    
    punctuation = ['.','?','!']
    if 