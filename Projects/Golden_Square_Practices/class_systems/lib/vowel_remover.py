# File: lib/vowel_remover.py
class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        print(f"i = {i}")
        while i < len(self.text):
            if self.text[i].lower() in self.vowels:
                self.text = self.text[:i] + self.text[i+1:]
                print(f"self.text[:i] = {self.text[:i]}")
                print(f"self.text[i+1:] = {self.text[i+1:]}")
            i += 1
        print(f"self.text = {self.text}")
        return self.text

remover = VowelRemover("We will remove the vowels from this sentence.")
print(remover.remove_vowels())