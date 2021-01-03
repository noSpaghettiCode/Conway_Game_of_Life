import pygame, sys
from random import randint
import numpy as np

# setup window

pygame.init()

width = 500
height = 500
objwidth = 100
objheight = 100

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('The Game Of Life')

def condition(blink, i, j):
    counter = 0
    if blink[i - 1][j - 1] == 1: counter += 1
    if blink[i - 1][j] == 1: counter += 1
    if blink[i - 1][j + 1] == 1: counter += 1
    if blink[i][j - 1] == 1: counter += 1
    if blink[i][j + 1] == 1: counter += 1
    if blink[i + 1][j - 1] == 1: counter += 1
    if blink[i + 1][j] == 1: counter += 1
    if blink[i + 1][j + 1] == 1: counter += 1  
    
    return counter

def GameOfLife(blink, auxBlink):
    for i in range(1, objheight - 1):
        for j in range(1, objwidth - 1):
            neighbours = condition(blink, i, j)
            if blink[i][j] == 1 and neighbours < 2 or neighbours > 3:
                auxBlink[i][j] = 0
            if blink[i][j] == 1 and neighbours == 2 or neighbours == 3:
                auxBlink[i][j] = 1
            if blink[i][j] == 0 and neighbours == 3:
                auxBlink[i][j] = 1

    for i in range(1, objheight - 1):
        for j in range(1, objwidth - 1):
            if auxBlink[i][j] == 1:
                pygame.draw.rect(win, (255, 255, 255), (i * 5, j * 5, 5, 5))
     

def main():

    clock = pygame.time.Clock()

    blink = np.random.randint(2, size=(objwidth, objheight))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        win.fill((0, 0, 0))
        
        auxBlink = np.zeros((objheight, objwidth))
        GameOfLife(blink, auxBlink)
        blink = auxBlink

        pygame.display.update()
        clock.tick(60)

main()