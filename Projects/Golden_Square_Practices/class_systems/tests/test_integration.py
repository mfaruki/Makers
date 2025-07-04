
from lib.diary import *
from lib.diary_entry import *
"""
test diary.add() and it should call an instance of the diary_entry() 
to add the title and contents of the diary entry
"""
def test_diary_add_function():
    diary = Diary()
    entry_1 = DiaryEntry("Monday 1st", "I walked my dog today")
    entry_2 = DiaryEntry("Tuesday 2nd", "I went to the musuem")
    diary.add(entry_1)
    diary.add(entry_2)
    result = diary.all()
    assert result == [entry_1, entry_2]


"""
test diary.count() and it should use the diary_entry.count_words() function 
to count the number of words in all entries, so it may be in a loop
"""
def test_diary_count_function():
    diary = Diary()
    entry_1 = DiaryEntry("Monday 1st", "I walked my dog today")
    entry_2 = DiaryEntry("Tuesday 2nd", "I went to the musuem")
    diary.add(entry_1)
    diary.add(entry_2)
    result = diary.count_words()
    assert result == 10
"""
test diary.reading_time() and it should use the diar_entry.reading_time() function
to return an rading time minutes
"""
def test_reading_time_function():
    diary = Diary()
    entry_1 = DiaryEntry("Monday 1st", "I walked my dog today")
    entry_2 = DiaryEntry("Tuesday 2nd", "I went to the musuem")
    diary.add(entry_1)
    diary.add(entry_2)
    result = diary.reading_time(2)
    assert result == 20

"""
test find_best_entry_for_reading_time() and it should use the 
"""