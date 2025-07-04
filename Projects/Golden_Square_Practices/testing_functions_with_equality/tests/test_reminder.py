# File: tests/test_reminder.py

from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

# We would typically have a number of these examples.
def test_reminder():
    reminder = Reminder("Kay")
    result = reminder.remind()
    assert result == "No reminder set!"