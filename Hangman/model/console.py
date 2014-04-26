'''
Created on Apr 23, 2014

@author: DFraser
'''
import unittest
import os
from model import Model
import random
import getpass
import json

class Console():
    def __init__(self):
        self.guesses = 0
        self.difficulty = ""
        self.max = 10
        self.words = {}
        self.file = os.path.join(os.getcwd(), "words.json")
        self.game = Model()

    def get_difficulty(self):
        self.difficulty = ""
        print("Enter your difficulty E-Easy, M-medium, H-hard:")
        while self.difficulty == "":
            d = raw_input()
            if d.lower() == "e":
                self.difficulty = "easy"
            elif d.lower() == 'm':
                self.difficulty = "medium"
            elif d.lower() == "h":
                self.difficulty = "hard"
            else:
                print("Not a valid difficulty")
                print("Re-enter a valid difficulty E-Easy, M-medium, H-hard:")
    
    def get_guess(self):
        print("Enter your letter guess:")
        letter = raw_input()
        return letter.lower()

    def fetch_words(self):
        json_data=open(self.file).read()
        data = json.loads(json_data)
        self.words = data
        return
    
    def set_word(self):
        playable = True
        if self.difficulty == "":
            self.fetch_words()
            self.get_difficulty()
        if len(self.words[self.difficulty]) == 0:
            self.increase_difficulty()
            if self.difficulty == "":
                playable = False
        if playable:
            word = self.words[self.difficulty].pop(random.randint(0,len(self.words[self.difficulty])-1))
            self.game.set_word(word['word'])
        return playable
    
    def increase_difficulty(self):
        if self.difficulty == "easy":
            self.difficulty = " medium"
        elif self.difficulty == "medium":
            self.difficulty = "hard"
        else:
            self.difficulty = ""
    
    def display(self):
        self.hangman()
        print(self.game.get_show())
    
    def hangman(self):
        if self.game.guesses == 1:
            print("/")
        elif self.game.guesses == 2:
            print("/ \\")
        elif self.game.guesses == 3:
            print(" |\n/ \\")
        elif self.game.guesses == 4:
            print("\ \n |\n/ \\")
        elif self.game.guesses == 5:
            print("\ / \n |\n/ \\")
        elif self.game.guesses == 6:
            print("\O/ \n |\n/ \\")
            print("Hanged man")

    def main(self):
        done = False
        print("Hello {0}".format(getpass.getuser()) )
        while not done:
            self.game.reset()
            play = self.set_word()
            if play:
                guessed = False
                while (self.game.get_show() != self.game.get_word() 
                       and not guessed and self.game.guesses < 6):
                    self.display()
                    guess = self.get_guess()
                    while len(guess) <= 0:
                        guess = self.get_guess()
                    if len(guess) == 1:
                        self.game.guess_letter(guess)
                    else:
                        guessed = self.game.guess_word(guess)
                if self.game.guesses == 6:
                    self.hangman()
                print("\nPlay Again (Y/N):")
                done = raw_input()
                if done.upper() == "Y":
                    done = False
                else:
                    done = True
            else:
                print("You beat the game all - star")
                done = True
        print("Bye {0}".format(getpass.getuser()))

class Test(unittest.TestCase):
    
    def setUp(self):
        self.console = Console()

    def tearDown(self):
        pass

    def test_fetch_words(self):
        self.console.difficulty = "Easy"
        self.console.fetch_words()
        expected = {u'medium': [{u'word': u'hey', u'interest': [u'nerd', u'interjection'], u'hint': u'Beginning of conversation'}, {u'word': u'there', u'interest': [u'nerd', u'grammar'], u'hint': u'Their cousin'}], u'hard': [{u'word': u'numerical analysis', u'interest': [u'computer', u'math'], u'hint': u"Math's best guess"}, {u'word': u'divide and conquer', u'interest': [u'computer', u'math'], u'hint': u'Goes hand in hand with Recursion'}], u'easy': [{u'word': u'hey', u'interest': [u'nerd', u'interjection'], u'hint': u'Beginning of conversation'}, {u'word': u'there', u'interest': [u'nerd', u'grammar'], u'hint': u'Their cousin'}]}
        self.assertEqual(expected, self.console.words)
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    c = Console()
    c.main()