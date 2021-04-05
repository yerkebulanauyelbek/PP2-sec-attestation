import pygame
from math import cos, sin
import math
pygame.init()
size=(900,600)
font=pygame.font.SysFont("times-new-roman",18,True,False)
BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
y_point=["1.00","0.75","0.50","0.25","0.00","-0.25","-0.50","-0.75","-1.00"]
x_point=['-3п',' -5п/2','-2п',' -3п/2','-п ',' -п/2 ',' 0 ',' п/2 ',' п ',' 3п/2',' 2п',' 5п/2',' 3п']
pii=math.pi
screen=pygame.display.set_mode(size)
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    screen.fill(WHITE)
    pygame.draw.rect(screen,BLACK,(60,40,752,522),3)
    for y in range(0,752,60):
        pygame.draw.line(screen,BLACK,[60,y+60],[810,y+60],1)
    for x in range(0,752,115):
        pygame.draw.line(screen,BLACK,[x+90,40],[x+90,561])
    pygame.draw.line(screen,BLACK,[60,300],[812,300],3)
    pygame.draw.line(screen,BLACK,[435,40],[435,559],3)
    for i in range(101,777):
        y1=239*sin((i-100)/112 * pii)
        y2=241*sin((i-99)/112 * pii)
        pygame.draw.aalines(screen,RED,True,[(i,297+y1),((i+1),297+y2)])
    for i in range(103,780,3):
        y1=239*cos((i-100)/112*pii)
        y2=241*cos((i-99)/112*pii)
        pygame.draw.aalines(screen,BLUE,True,[(i,300+y1),((i+1),300+y2)])
    cnt=0
    for i in range(50,291,58):
        text=font.render(y_point[cnt],True,BLACK)
        screen.blit(text,(5,i))
        cnt+=1
    cnt1=5
    for i in range(343,553,60):
        text=font.render(y_point[cnt1],True,BLACK)
        screen.blit(text,(8,i))
        cnt1+=1
    cnt2=0
    for i in range(85,777,57):
        text=font.render(x_point[cnt2],True,BLACK)
        screen.blit(text,(i,559))
        cnt2+=1
    pygame.display.update()
    pygame.display.flip()
pygame.quit()