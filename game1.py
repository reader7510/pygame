
# example use min pygme

import pygame,sys

screen=600,400

pygame.init()

pygame.display.set_mode(screen)
pygame.display.set_caption("Dream")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pygame.display.update()
