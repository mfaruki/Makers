from lib.todo import *
import pytest

todo_list = TODO()
"""
first check if i can add en empty string
should raise an exception 
"""

def test_add_empty_string_task():
    with pytest.raises(Exception) as err:
        todo_list.add_task(" ")
    error_message = str(err.value)
    assert error_message == "Please add a string"


"""
add a string with no #TODO in the string 
should not add the string to the task list but should display the current tasks
"""

def test_add_string_with_no_todo():
    result = todo_list.add_task("walk my dog")
    assert result == []


"""
add a correct string to the add_task function and should add it to the task list and display it
"""
def test_add_string_with_todo():
    result = todo_list.add_task("walk my dog #TODO")
    assert result == ["walk my dog #TODO"]

"""
add multiple tasks both correct and incorrect to the add_task funcition ad it should sort them accordingly and display the corect ones. 
"""
def test_add_multiple_string_with_and_without_todo():
    todo_list.add_task("#TODO Buy groceries") #add
    todo_list.add_task("Finish homework #TODO")#add
    todo_list.add_task("Call mum") #dont add
    todo_list.add_task("#TODO Submit assignment")#add
    todo_list.add_task("Schedule dentist appointment")#dont add
    todo_list.add_task("Reply to emails")#dont add
    todo_list.add_task("Prepare meeting slides #TODO")#add
    todo_list.add_task("#TODO Clean the kitchen")#add
    todo_list.add_task("Go jogging")#dont add
    result = todo_list.add_task("#TODO Read Python documentation")#add

    assert result == [ 
        "walk my dog #TODO",
        "#TODO Buy groceries",
        "Finish homework #TODO",
        "#TODO Submit assignment",
        "Prepare meeting slides #TODO",
        "#TODO Clean the kitchen",
        "#TODO Read Python documentation"
]


"""
test the completed_task function with an empty string should raise and exception
and dsiplay the current task_list
"""
def test_remove_task_with_empty_string():
    with pytest.raises(Exception) as err:
        todo_list.completed_task(" ")
    error_message = str(err.value)
    assert error_message == "Please give a correct task to remove"

"""
test the completed_task function with an incorrect string and should say that that task does not exist
"""
def test_remove_task_with_incorrect_task():
    with pytest.raises(Exception) as err:
        todo_list.completed_task("this is a wrong task")
    error_message = str(err.value)
    assert error_message == "That task does not exist"


"""
test the completed_task() function with a correct string and it should remove it and display the updated list
"""
def test_remove_task_with_correct_task():
    result = todo_list.completed_task("#TODO Read Python documentation")
    assert result == result == [ 
        "walk my dog #TODO",
        "#TODO Buy groceries",
        "Finish homework #TODO",
        "#TODO Submit assignment",
        "Prepare meeting slides #TODO",
        "#TODO Clean the kitchen"
    ]

"""
test mutiple removals and additions to the task list and it should do it accuratley
"""
def test_multiple_task_additions_and_removals():
    task_list = TODO()
    #add 10 tasks some are incorrect
    task_list.add_task("#TODO Buy groceries")
    task_list.add_task("Finish homework #TODO")
    task_list.add_task("Call mum")
    task_list.add_task("#TODO Submit assignment")
    task_list.add_task("Schedule dentist appointment")
    task_list.add_task("Reply to emails")
    task_list.add_task("Prepare meeting slides #TODO")
    task_list.add_task("#TODO Clean the kitchen")
    task_list.add_task("Go jogging")
    task_list.add_task("#TODO Read Python documentation")

    #remove 5 tasks some are incorrect
    task_list.completed_task("#TODO Buy groceries")
    task_list.completed_task("Prepare meeting slides #TODO")
    result = task_list.completed_task("#TODO Read Python documentation")

    assert result == [
        "Finish homework #TODO",
        "#TODO Submit assignment",
        "#TODO Clean the kitchen"
    ]