def make_snippet(input_string):

    if not isinstance(input_string, str):
        raise TypeError("Parameter 'input_string' must be type String")
    
    if len(input_string) > 0 and input_string != " ":
        list_of_string = input_string.split()
    else:
        return "Snippet is empty"

    if len(list_of_string) <= 5:
        return input_string
    else:
        return " ".join(list_of_string[:5]) + "..."