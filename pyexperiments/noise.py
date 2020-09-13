import pygame
import random
sc = pygame.display.set_mode ([512, 512])
timer = pygame.time.Clock()
keep_going = True
bg_color = (0, 0, 0)
x = 0
y = 0
slise = 5
size = 500
sx = 100
sy = 150
xposes = [sx]
yposes = [sy]
clr = 0
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            keep_going = False
    for x in range(0, 512):
        for y in range(0, 512):
            clr = random.random()
            pygame.draw.line(sc, ((clr, clr, clr)),
            [y, x], [y, x])
        pygame.display.update()
