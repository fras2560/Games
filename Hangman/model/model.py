'''
@author: Dallas Fraser
@contact: fras2560@mylaurier.ca
@version: 1.0
@date: 23/04/2014
@note: This model of the hangman game
'''
import unittest

class Model():
    def __init__(self):
        self.word = []
        self.guessed = []
        self.show = []
        self.guesses = 0
        
    def reset(self):
        del self.word[:]
        del self.guessed[:]
        del self.show[:]
        
    def set_word(self,word):
        word = word.lower()
        for letter in word:
            self.word.append(letter)
            if(letter != " "):
                self.show.append("*")
            else:
                self.show.append(" ")

    def get_word(self):
        return "".join(self.word)
    
    def get_show(self):
        return "".join(self.show)
    
    def guess_letter(self,guess):
        if guess not in self.guessed:
            correct = 0
            pos = 0
            for letter in self.word:
                if letter == guess:
                    correct += 1
                    self.show[pos] = letter
                pos += 1
            self.guessed.append(guess)
        else:
            correct = -1
        if correct == 0:
            self.guesses += 1
        return correct

    def guess_word(self,word):
        if not self.get_word() == word:
            self.guesses += 1
        return self.get_word() == word
    
class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = Model()
    
    def tearDown(self):
        pass
    
    def test_reset(self):
        self.model.word = ['a','2']
        self.model.guessed = ['a']
        self.model.show = []
        self.model.reset()
        self.assertEqual(self.model.word,[])
        self.assertEqual(self.model.guessed, [])
        self.assertEqual(self.model.show,[])
    
    def test_set_word(self):
        self.model.set_word("hey")
        self.assertEqual(self.model.word, ['h','e','y'])
        self.assertEqual(self.model.show, ['*','*','*'])
        self.model.word = []
        self.model.show = []
        self.model.set_word("hey there")
        self.assertEqual(self.model.word, ['h','e','y', ' ', 't', 'h', 'e', 'r', 'e'])
        self.assertEqual(self.model.show, ['*','*','*', ' ',  '*', '*', '*', '*','*',])

    def test_get_word(self):
        self.model.word = ['h','e','y']
        word = self.model.get_word()
        self.assertEqual(type(word), str )
        self.assertEqual(word, "hey")

    def test_get_show(self):
        self.model.show = ["*","y"]
        show = self.model.get_show()
        self.assertEqual(type(show), str )
        self.assertEqual(show, "*y")

    def test_guess_letter(self):
        self.model.word = ['h','e','y']
        self.model.show = ['*','*','*']
        correct = self.model.guess_letter('h')
        self.assertEqual(type(correct), int)
        self.assertEqual(correct, 1)
        self.assertEqual(self.model.show, ['h','*','*'])
        self.assertEqual(self.model.guessed, ['h'])
        self.assertEqual(self.model.guesses, 0)
        correct = self.model.guess_letter('a')
        self.assertEqual(type(correct), int)
        self.assertEqual(correct, 0)
        self.assertEqual(self.model.show, ['h','*','*'])
        self.assertEqual(self.model.guessed, ['h','a'])
        self.assertEqual(self.model.guesses, 1)
        correct = self.model.guess_letter('h')
        self.assertEqual(type(correct), int)
        self.assertEqual(correct, -1)
        self.assertEqual(self.model.show, ['h','*','*'])
        self.assertEqual(self.model.guessed, ['h','a'])
        self.assertEqual(self.model.guesses, 1)
        
    def test_guess_word(self):
        self.model.word = ['h','e','y']
        self.assertEqual(self.model.guess_word("hey"), True)
        self.assertEqual(self.model.guesses, 0)
        self.assertEqual(self.model.guess_word("hay"), False)
        self.assertEqual(self.model.guesses, 1)
        