
# example use  pygme move speed fps,KEYBAORD ctrl,resize,ico,RESIZABLE

import pygame,sys
pygame.init()
size= width,height=600,400
speed=[1,1]
BLACK=0,0,0
fps=300  #every send 300
fclock=pygame.time.Clock()

screen=pygame.display.set_mode(size,pygame.RESIZABLE)
#screen=pygame.display.set_mode(size,pygame.NOFRAME)
#screen=pygame.display.set_mode(size,pygame.FULLSCREEN)
pygame.display.set_caption("Dream")
ball=pygame.image.load("ball.jpg")
icon= pygame.image.load("Green_Time.ico")
pygame.display.set_icon(icon)
ballrect=ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0]=speed[0] if speed[0]==0 else (abs(speed[0])-1)*int(speed[0]/abs(speed[0]))
            if event.key == pygame.K_RIGHT:
                speed[0]=speed[0]+1
            if event.key == pygame.K_UP:
                speed[1]=speed[1]+1
            if event.key == pygame.K_DOWN:
                speed[1]=speed[1]-1
                if speed[1]<=0 :
                    speed[1]=0
            if event.key == pygame.K_ESCAPE:
                sys.exit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0],event.size[1]
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    if pygame.display.get_active():
        ballrect=ballrect.move(speed[0],speed[1])
    if ballrect.left<0 or ballrect.right>width:
        speed[0]=-speed[0]
    if ballrect.top<0 or ballrect.bottom>height:
        speed[1]=-speed[1]
    screen.fill(BLACK)
    screen.blit(ball,ballrect)
    pygame.display.update()
    fclock.tick(fps)
