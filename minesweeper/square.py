'''
Created on Oct 18, 2015

@author: Dallas
'''
import unittest
import pygame

from minesweeper.settings import BLACK, SQUARE
class Square():
    def __init__(self, x=None, y=None):
        self.flagged = False
        self.bombed = False
        self.x = x
        self.y = y
        self.mark = False
        self.neighbors = 0
        self.covered = True
        
    def uncover(self):
        self.covered = False

    def is_covered(self):
        return self.covered

    def flag(self):
        self.flagged = not self.flagged

    def is_flagged(self):
        return self.flagged

    def question(self):
        self.mark = not self.mark

    def is_questioned(self):
        return self.mark

    def bomb(self):
        self.bombed = not self.bombed

    def is_bombed(self):
        return self.bombed

    def number(self, x):
        self.neighbors = x

    def get_number(self):
        return self.neighbors

    def draw(self, surface):
        print(self.x , self.y)
        if self.covered:
            pygame.draw.rect(surface, BLACK, (self.x, self.y, SQUARE, SQUARE), 1)
        else:
            header = pygame.font.SysFont('monospace', 18)
            label = header.render(str(self.neighbors), 2, BLACK)
            surface.blit(label, (self.x, self.y))
class Test(unittest.TestCase):

    def setUp(self):
        self.square = Square()

    def testAll(self):
        # test is bomb
        result = self.square.is_bombed()
        self.assertEqual(result, False)
        self.square.bomb()
        result = self.square.is_bombed()
        self.assertEqual(result, True)
        # test is question
        result = self.square.is_questioned()
        self.assertEqual(result, False)
        self.square.question()
        result = self.square.is_questioned()
        self.assertEqual(result, True)
        # test flag
        result = self.square.is_flagged()
        self.assertEqual(result, False)
        self.square.flag()
        result = self.square.is_flagged()
        self.assertEqual(result, True)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()