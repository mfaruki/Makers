class GrammarStats:
    def __init__(self):
        self.test_marks = []

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        punctuation = ['.' , '!' , '?']
        if text.strip() == "":
            return "Please provide a string"
        elif text[-1] in punctuation and text[0].isupper() == True:
            self.test_marks.append(True)
            return True
        else:
            self.test_marks.append(False)
            return False 


    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if not self.test_marks:
            return 0
        total_passed = self.test_marks.count(True)
        pass_marks = (total_passed/len(self.test_marks)) * 100
        print(pass_marks)
        return pass_marks

