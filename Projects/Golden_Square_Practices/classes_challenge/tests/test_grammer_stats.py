from lib.grammer_stats import *

"""
test check() with an empty string and should return "Please provide a string"

"""
def test_check_with_empty_string():
    grammer_check = GrammarStats()
    result = grammer_check.check("")
    assert result == "Please provide a string"

def test_check_with_correct_string():
    grammer_check = GrammarStats()
    result = grammer_check.check("She smiled softly.")
    assert result == True

def test_check_with_incorrect_string_no_capital():
    grammer_check = GrammarStats()
    result = grammer_check.check("she smiled softly.")
    assert result == False

def test_check_with_incorrect_string_no_punctuation():
    grammer_check = GrammarStats()
    result = grammer_check.check("She smiled softly")
    assert result == False

def test_check_percentage_good():
    grammer_check = GrammarStats()
    grammer_check.check("She smiled softly.") #True
    grammer_check.check("Dreams come true!")#True
    grammer_check.check("She whispered gently.")#True
    grammer_check.check("I waited quietly.")#True
    grammer_check.check("They laughed loudly")#False
    grammer_check.check("time moves fast.") #False
    grammer_check.check("Dreams come true!")#True
    grammer_check.check("Dreams come true?")#True
    result = grammer_check.percentage_good()
    assert result == 75

def test_check_percentage_good_all_fail():
    grammer_check = GrammarStats()
    grammer_check.check("She smiled softly") 
    grammer_check.check("reams come true!")
    grammer_check.check("She whispered gently")
    grammer_check.check("waited quietly.")
    grammer_check.check("They laughed loudly")
    grammer_check.check("time moves fast") 
    grammer_check.check("reams come true!")
    grammer_check.check("Dreams come true")
    result = grammer_check.percentage_good()
    assert result == 0