import pygame
import math
sc = pygame.display.set_mode ([900,600])
timer = pygame.time.Clock()
keep_going = True
bg_color = (255, 200, 210)
x = 0
y = 0
size = 10

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            keep_going = False
    #sc.fill(bg_color)
    pygame.draw.line(sc, (pygame.mouse.get_pos()[0]/ 900*255, pygame.mouse.get_pos()[1]/ 600*255, pygame.mouse.get_pos()[0]/ 900*255), [int(math.sin(y)*size) + pygame.mouse.get_pos()[0]  , int(math.sin(x)*size) +pygame.mouse.get_pos()[1]], [int(math.sin(x)*size) + pygame.mouse.get_pos()[0], int(math.sin(y)*size) + pygame.mouse.get_pos()[1]], 2)
    pygame.display.update()
    timer = pygame.time.Clock()
