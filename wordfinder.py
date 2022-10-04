"""Word Finder: finds random words from a dictionary."""
from random import choice

class WordFinder:
    """Finds words in a file and makes attributes of those words
    >>> t = WordFinder('words.txt')
    
    
    """
    def __init__(self,path):
        self.path = path
        self.words_list = []
        self.make_attributes()
        print(f"{len(self.word_list)} words read")
    def make_attributes(self):
        open_file = open(self.path)
        all_text = open_file.read()
        self.word_list = all_text.split('\n')
        open_file.close()
    def random(self):
        return choice(self.word_list)

class SpecialWordFinder(WordFinder):
    """returns a food if it is a category that starts with a # sign, ignore the blank lines"""
    def random(self):
        """if user specifies a category then return a random list of foods from that category only"""
        return choice([w for w in self.word_list if w !="" and not w.startswith("#")])
        