'''
Created on Mar 30, 2014

@author: Dallas
'''
import unittest
import pygame
import matrix
import piece
'''
-----------
GAME FUNCTIONS
-----------
'''

def draw(size):
    height_pos = 0
    for r in game._matrix:
        width_pos = 0
        for cell in r:
            if cell == 0 :
                pass
            else:
                pygame.draw.rect(screen,GREEN,[width_pos,height_pos,size,size])
            width_pos += size
        height_pos += size

def draw_grid(size):
    #draw rows
    height_pos = 0
    for r in game._matrix:
        pygame.draw.lines(screen,BLACK,0,[(0,height_pos),(WIDTH,height_pos)])
        height_pos += size
    #draw columns
    width_pos = 0
    for r in game._matrix[0]:
        pygame.draw.lines(screen,BLACK,0,[(width_pos,0),(width_pos,HEIGHT)])
        width_pos += size

def draw_piece(size):
    points  = tetris.return_points()
    for point in points:
        x = point[0][0]
        y = point[1][0]
        width_pos = x * size
        height_pos = y * size
        pygame.draw.rect(screen,RED,[width_pos,height_pos,size,size])

def draw_shadow(size):
    moves = 0
    while game.move_down(tetris):
        moves +=1
    points  = tetris.return_points()
    for point in points:
        x = point[0][0]
        y = point[1][0]
        width_pos = x * size
        height_pos = y * size
        pygame.draw.rect(screen,GREY,[width_pos,height_pos,size,size])
    tetris.translate(0,-moves)

def display_game_over():
    label = myfont.render("GAME OVER!!",1,BLACK)
    x = WIDTH/2 - 100
    if x < 0:
        x = 0
    screen.blit(label,(x,HEIGHT/2))

def game_loop():
    done = False
    DOWN = LEVEL
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
                if key[pygame.K_s]:
                    moved = game.move_down(tetris)
                    if not moved:
                        game.add_piece(tetris)
                        tetris.create_piece()
                        tetris.translate(WIDTH/(2*SIZE), 1)
                        DOWN = LEVEL
                        if not game.check_valid(tetris):
                            done = True
                if key[pygame.K_SPACE]:
                    while game.move_down(tetris):
                        pass
                    game.add_piece(tetris)
                    tetris.create_piece()
                    tetris.translate(WIDTH/(2*SIZE), 1)
                    DOWN = LEVEL
        screen.fill(WHITE)
        if DOWN <=0:
            DOWN = LEVEL
            moved = game.move_down(tetris)
            if not moved:
                game.add_piece(tetris)
                tetris.create_piece()
                tetris.translate(WIDTH/(2*SIZE), 1)
                if not game.check_valid(tetris):
                    done = True
        game.print_m()
        game.check_lines()
        DOWN -= 1
        draw_grid(SIZE)
        draw(SIZE)
        draw_shadow(SIZE)
        draw_piece(SIZE)
        pygame.display.flip()
        clock.tick(10)
'''
---------------
GAME SETTINGS
---------------
'''
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
GREY     = ( 122,  122, 122)
SIZE = 10
WIDTH = 100
HEIGHT = 300
LEVEL = 10
DOWN = LEVEL
'''
---------------
STARTING STEPS
---------------
'''
tetris = piece.Piece()
game = matrix.Matrix(row=HEIGHT/SIZE,column=WIDTH/SIZE)
pygame.init()
size=(WIDTH,HEIGHT)
myfont = pygame.font.SysFont("monospace", 15)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tetris")
pygame.key.set_repeat(10,10)
done = False
tetris.create_piece()
tetris.translate(WIDTH/(2*SIZE), 1)
clock = pygame.time.Clock()
quit = False
play = True
while not quit:
    if play:
        game_loop()
        print("\n\n GAME OVER \n\n")
        display_game_over()
        pygame.display.flip()
    play = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if key[pygame.K_r]:
                game.initialize(HEIGHT/SIZE,WIDTH/SIZE)
                play = True

pygame.quit()
'''
---------------
ENDING STEPS
---------------
'''
