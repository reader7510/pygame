
# example use  pygme move speed fps

import pygame,sys

size= width,height=600,400
speed=[1,1]
BLACK=0,0,0
fps=300  #every send 300
fclock=pygame.time.Clock()

pygame.init()

screen=pygame.display.set_mode(size)
pygame.display.set_caption("Dream")
ball=pygame.image.load("ball.jpg")
ballrect=ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect=ballrect.move(speed[0],speed[1])
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]
    screen.fill(BLACK)
    screen.blit(ball,ballrect)
    pygame.display.update()
    fclock.tick(fps)
