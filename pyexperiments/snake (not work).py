import pygame
import time
sc = pygame.display.set_mode ([200, 300])
timer = pygame.time.Clock()
keep_going = True
bg_color = (255, 255, 255)
x = 0
y = 0
angle = 75
size = 100
sx = 100
sy = 150
xposes = [sx, sx, sx, sx, sx, sx, sx]
yposes = [sy+20, sy+40, sy+60, sy+80, sy+100, sy+120, sy+10]

for d in range(0, 70):
    sc.fill(bg_color)
    keys = pygame.key.get_pressed()
    if keys [pygame.K_d]:
        xposes[len(xposes)-1] += 1
    if keys [pygame.K_a]:
        xposes[len(xposes)-1] -= 1
    if keys [pygame.K_s]:
        yposes[len(yposes)-1] += 1
    if keys [pygame.K_w]:
        yposes[len(yposes)-1] -= 1
    for c in range(0, len(xposes)-2):
        pygame.draw.line(sc, ((0, 0, 0)),[int(xposes[c]), int(yposes[c])], [int(xposes[c+1]), int(yposes[c+1])])
        xposes[c] += (xposes[c] - xposes[c+1])/5
        yposes[c] += (yposes[c] - yposes[c+1]) / 5
        time.sleep(0.1)
        pygame.display.update()
time.sleep(10)