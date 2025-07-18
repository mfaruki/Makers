class DiaryEntry:
    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   contents: string
        self.title = title
        self.contents = contents
        self.bookmark = 0

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        return f"{self.title} : {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        return len(self.contents.split(" "))

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        number_of_words = self.count_words()
        reading_time = number_of_words/wpm
        return reading_time

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        words_user_can_read = wpm*minutes
        list_of_words = self.contents.split(" ")
        if words_user_can_read > len(list_of_words) - self.bookmark:
            chunk = " ".join(list_of_words[self.bookmark:])
            self.bookmark = 0
            return chunk

        else:
            chunk = " ".join(list_of_words[self.bookmark:self.bookmark+words_user_can_read])
            self.bookmark += words_user_can_read
            return chunk
