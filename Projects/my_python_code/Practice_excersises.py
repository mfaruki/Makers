def add_two_numbers(a, b):
    """
    This function takes two numbers and returns their sum.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    
    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b

def add_three_numbers(a, b, c):
    """
    This function takes three numbers and returns their sum.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.
    c (int or float): The third number.
    
    Returns:
    int or float: The sum of the three numbers.
    """
    return a + b + c

def concat_names(first_name, second_name, third_name):
    """
    This function concatenates three names into a single string.
    
    Parameters:
    first_name (str): The first name.
    second_name (str): The second name.
    third_name (str): The third name.
    
    Returns:
    str: A string containing all three names separated by spaces.
    """
    return f"Hello {first_name}, {second_name}, {third_name}, welcome to the Python world!"\
    

def superify(name):
    return f'super{name}'


# Don't edit below this line.

dog_result = superify("dog")
print(f"Look, it's {dog_result}!")
# Should print "Look, it's superdog!"

cat_result = superify(superify(superify("cat")))
print(f"Look, it's {cat_result}!")
# Should print "Look, it's supersupersupercat!"
