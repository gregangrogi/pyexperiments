import pygame
import math
sc = pygame.display.set_mode ([200, 300])
timer = pygame.time.Clock()
keep_going = True
bg_color = (0, 0, 0)
x = 0
y = 0
angle = 75
size = 100
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

    sc.fill(bg_color)
    x = pos(angle)[0] * 2
    y = pos(angle)[1] * 2
    for c in range(0, size):
        if xposes[c]<0 or xposes[c]>200:
            x = -x
        if yposes[c] < 0 or yposes[c] > 300:
            y = -y
        pygame.draw.line(sc, ((255-(c / size * 200), 255-(c / size * 100), 255-(c / size * 100))), [xposes[c], yposes[c]], [int(xposes[c] + x), int(yposes[c] + y)])
        xposes.append(xposes[c] + x)
        yposes.append(yposes[c] + y)
    del xposes[:]
    del yposes[:]
    xposes = [sx]
    yposes = [sy]
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        angle += 0.001
    if keys[pygame.K_e]:
        angle -= 0.001
    if keys[pygame.K_w]:
        size += 1
    if keys[pygame.K_s]:
        size -= 1
    pygame.display.update()