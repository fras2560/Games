'''
Created on Mar 30, 2014

@author: Dallas
'''
import unittest
import pygame
import matrix
import piece

def draw(size):
    height_pos = 0
    for r in game._matrix:
        width_pos = 0
        for cell in r:
            if cell == 0 :
                pass
            else:
                pygame.draw.rect(screen,RED,[width_pos,height_pos,size,size])
            width_pos += size
        height_pos += size


BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

tetris = piece.Piece()
game = matrix.Matrix(row=30,column=10)
pygame.init()
size=(100,300)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tetris")
done = False
tetris.create_piece()
game.add_piece(tetris)    
clock = pygame.time.Clock()
down = 2
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_d]:
                game.move_right(tetris)
            if key[pygame.K_a]:
                game.move_left(tetris)
            if key[pygame.K_w]:
                game.rotate_piece(tetris)
    screen.fill(WHITE)
    if down <=0:
        down = 2
        moved = game.move_down(tetris)
        if not moved:
            tetris.create_piece()
            game.add_piece(tetris)
    game.print_m()
    game.check_lines()
    down -= 1
    draw(10)
    pygame.display.flip()
    clock.tick(10)
    
pygame.quit()
