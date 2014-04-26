'''
Created on Apr 24, 2014

@author: DFraser
'''
import unittest
import json
import pygame
from model import Model
import random
import os
SIZE = [700,500]

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
MARGIN = 100
SPACE = 10

class GUI():
    def __init__(self):
        self.pygame = pygame.init()
        self.game = Model()
        self.words = []
        self.score = 0
        self.difficulty = "easy"
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Hangman")
        self.header = pygame.font.SysFont("monospace", 36)
        self.point = pygame.font.SysFont('monospace', 18)
        self.file = os.path.join(os.getcwd(), "words.json")
        self.over = False
    def increase_difficulty(self):
        if self.difficulty == "easy":
            self.difficulty = "medium"
        elif self.difficulty == "medium":
            self.difficulty = "hard"
        else:
            self.difficulty = ""
    
    def fetch_words(self):
        json_data=open(self.file).read()
        data = json.loads(json_data)
        self.words = data
        return
    
    def set_word(self):
        playable = True
        print(self.words)
        if self.difficulty == "":
                playable = False
        if playable:
            if len(self.words[self.difficulty]) == 0:
                self.increase_difficulty()
                if self.difficulty == "":
                    playable = False
        if playable:
            pos = len(self.words[self.difficulty])-1
            word = self.words[self.difficulty].pop(random.randint(0,pos))
            self.game.set_word(word['word'])
        return playable

    def display_guessed(self):
        output = "Guesses:"
        for guess in self.game.guessed:
            output += "  " + guess
        label = self.point.render(output,1,BLACK)
        self.screen.blit(label,(MARGIN,SIZE[1] - MARGIN))

    def display_word(self):
        if not self.over:
            output = self.game.get_show()
        else:
            output = self.game.get_word()
        label = self.header.render(output,1,BLACK)
        self.screen.blit(label,(SIZE[0]/2 - 100,SIZE[1]/2))

    def draw_hangman(self):
        self.draw_foundation()
        middle = MARGIN + 200 - 10
        radius = 20
        top = 60 + radius
        length = 40
        if self.game.guesses > 0:
            #head
            pygame.draw.circle(self.screen,BLACK,(middle,top),radius,1)
        if self.game.guesses > 1:
            #neck
            pygame.draw.line(self.screen, BLACK,(middle,top+radius),
                             (middle,top+radius+length))
        if self.game.guesses > 2:
            #left arm
            pygame.draw.line(self.screen, BLACK,(middle,top+radius+length),
                             (middle-length/2,top+length/2))
        if self.game.guesses > 3:
            #right arm
            pygame.draw.line(self.screen, BLACK,(middle,top+radius+length),
                             (middle+length/2,top+length/2))
        if self.game.guesses > 4:
            #torso
            pygame.draw.line(self.screen, BLACK,(middle,top+length),
                             (middle,top+2*length))
        if self.game.guesses > 5:
            #left leg
            pygame.draw.line(self.screen, BLACK,(middle,top+2*length),
                             (middle-length/2,top+2*length+length/2))
        if self.game.guesses > 6:
            #right leg
            pygame.draw.line(self.screen, BLACK,(middle,top+2*length),
                             (middle+length/2,top+2*length+length/2))

    def draw_foundation(self):
        #left post
        pygame.draw.rect(self.screen,BLACK,(MARGIN,20,20,SIZE[1]-MARGIN-40),1)
        #top post
        pygame.draw.rect(self.screen,BLACK,(MARGIN,0,200,20),1)
        #right post
        pygame.draw.rect(self.screen,BLACK,(MARGIN+200-20,20,20,40),1)
        #bottom post
        pygame.draw.rect(self.screen,BLACK,(MARGIN-40,SIZE[1]-MARGIN-20,100,20),1)
        # supporting beams
        pygame.draw.line(self.screen,BLACK,(MARGIN+20,MARGIN),(MARGIN+40,20),1)
    
    def draw_gameover(self):
        output = "Hanged my man: Y to play again"
        label = self.header.render(output,1,BLACK)
        self.screen.blit(label,(SIZE[0]/2 - 200,SIZE[1]/2-30))
    
    def winner(self):
        output = "All star: you have won"
        label = self.header.render(output,1,BLACK)
        self.screen.blit(label,(SIZE[0]/2 - 200,SIZE[1]/2-30))
    
    def apply_game_rules(self):
        if self.game.guesses > 6:
            self.over = True
            self.draw_gameover()
        if self.game.get_word() == self.game.get_show():
            self.game.reset()
            play = self.set_word()
            if not play:
                self.winner()
    
    def game_restart(self):
        self.game.reset()
        play = self.set_word()
        if play:
            self.over = False
        else:
            self.winner()
    def main(self):
        self.fetch_words()
        done = False
        self.set_word()
        while not done:
            for event in pygame.event.get(): # User did something
                if event.type == pygame.QUIT: # If user clicked close
                    done = True # Flag that we are done so we exit this loop
                elif event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    if key[pygame.K_a]:
                        self.game.guess_letter("a")
                    elif key[pygame.K_b]:
                        self.game.guess_letter("b")
                    elif key[pygame.K_c]:
                        self.game.guess_letter("c")
                    elif key[pygame.K_d]:
                        self.game.guess_letter("d")
                    elif key[pygame.K_e]:
                        self.game.guess_letter("e")
                    elif key[pygame.K_f]:
                        self.game.guess_letter("f")
                    elif key[pygame.K_g]:
                        self.game.guess_letter("g")
                    elif key[pygame.K_h]:
                        self.game.guess_letter("h")
                    elif key[pygame.K_i]:
                        self.game.guess_letter("i")
                    elif key[pygame.K_j]:
                        self.game.guess_letter("j")
                    elif key[pygame.K_k]:
                        self.game.guess_letter("k")
                    elif key[pygame.K_l]:
                        self.game.guess_letter("l")
                    elif key[pygame.K_m]:
                        self.game.guess_letter("m")
                    elif key[pygame.K_n]:
                        self.game.guess_letter("n")
                    elif key[pygame.K_o]:
                        self.game.guess_letter("o")
                    elif key[pygame.K_p]:
                        self.game.guess_letter("p")
                    elif key[pygame.K_q]:
                        self.game.guess_letter("q")
                    elif key[pygame.K_r]:
                        self.game.guess_letter("r")
                    elif key[pygame.K_s]:
                        self.game.guess_letter("s")
                    elif key[pygame.K_t]:
                        self.game.guess_letter("t")
                    elif key[pygame.K_u]:
                        self.game.guess_letter("u")
                    elif key[pygame.K_v]:
                        self.game.guess_letter("v")
                    elif key[pygame.K_w]:
                        self.game.guess_letter("w")
                    elif key[pygame.K_x]:
                        self.game.guess_letter("x")
                    elif key[pygame.K_y]:
                        if self.over:
                            self.game_restWart()
                        else:
                            self.game.guess_letter("y")
                    elif key[pygame.K_z]:
                        self.game.guess_letter("z")
            self.screen.fill(WHITE)
            self.display_guessed()
            self.display_word()
            self.draw_hangman()
            self.apply_game_rules()
            pygame.display.flip()
        pygame.quit()


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    game = GUI()
    game.main()