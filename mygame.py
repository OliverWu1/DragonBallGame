import pygame
import sys
from utils import playerMovement
import time

pygame.init()


screen = pygame.display.set_mode((1150, 1150))
Background = pygame.image.load('resources/imagens/openning/background/goku-vs-vegeta-2.jpg')
pm = playerMovement()
screen.blit(Background, (0, 0))
x = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    x = x+1
    screen.blit(Background, (0,0) )
    pm.gokuRun(screen = screen, x = x, y= 100)
    pygame.display.update()
    time.sleep(0.1)



 