'''
Created on Oct 18, 2015

@author: Dallas
'''
from minesweeper.map import Map
import pygame
from minesweeper.settings import SIZE, MARGIN, WHITE, SQUARE, BLACK
class game():
    def __init__(self):
        pygame.init()
        self.game = Map((SIZE[0] - MARGIN) // SQUARE,
                        (SIZE[1] - MARGIN) // SQUARE)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Rampart")

    def controls(self):
        keys = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #right click
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]
                if self.in_bounds(x, y) and event.button == 3:
                    # right click
                    self.game.right_click (x, y)
                elif  self.in_bounds(x, y) and event.button == 1:
                    # left click
                    self.game.left_click (x, y)

    def in_bounds(self, x, y):
        return (x > MARGIN or x < SIZE[0] - MARGIN) and\
                (y > MARGIN or y < SIZE[1] - MARGIN)

    def game_loop(self):
        done = False
        while not done:
            self.controls()
            self.screen.fill(WHITE)
            self.clock.tick(10)
            self.game.draw(self.screen)
            pygame.display.flip()

if __name__ == "__main__":
    g = game()
    g.game_loop()
