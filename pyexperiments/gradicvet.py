import pygame
import math
sc = pygame.display.set_mode ([500, 500])
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
def pos(angle):
    x = math.sin(angle)
    y = math.cos(angle)
    return[x, y]

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            keep_going = False
    for f in range(0, slise):
        pygame.draw.rect(sc, (f/slise*255, 255 - f/slise*255, 255), (0, int(size/slise*f), 500, int(size/slise)))
        pygame.display.update()
        keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        slise +=1
    if keys[pygame.K_e]:
        if slise > 3:
            slise -=1