import pygame
import math
sc = pygame.display.set_mode ([900,600])
timer = pygame.time.Clock()
keep_going = True
bg_color = (55, 0, 10)
x = 500
y = 200
angle = 75
size = 100
sx = 100
sy = 100
ssize = 50
xposes = [x]
yposes = [y]
def pos(angle):
    x = math.sin(angle)
    y = math.cos(angle)
    return[x, y]
def sphere (pos, size, lpos):
    ww =((lpos[0]-pos[0])**2) + ((lpos[1]-pos[1])**2)
    width = math.sqrt(abs(ww))
    
    #print (abs(ww))
    return width - size
print (sphere([sx, sy], ssize, [x, y]))

while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            keep_going = False

    sc.fill(bg_color)
    #pygame.draw.rect(sc, (255, 255, 255), (20, 20, 100, 75))
    for r in range(0, 100):
        size = int(sphere([sx, sy], ssize, [xposes[r], yposes[r]]))
        pygame.draw.line(sc, ((255, 255, 255)), [x+int(pos(angle)[0]*size), y+int(pos(angle)[1]*size)], [xposes[r], yposes[r]])
        xposes.append(x+int(pos(angle)[0]*size))
        yposes.append(y+int(pos(angle)[1]*size))
    del xposes[:]
    del yposes[:]
    xposes = [x]
    yposes = [y]
    for d in range(0, 360):
        pygame.draw.line(sc, ((255, 255, 255)), [sx+int(pos(d)[0]*ssize), sy+int(pos(d)[1]*ssize)], [sx, sy])
    keys = pygame.key.get_pressed()
    if keys [pygame.K_q]:
        angle += 0.01
    if keys [pygame.K_e]:
        angle -= 0.01
    if keys [pygame.K_d]:
        sx += 1
    if keys [pygame.K_a]:
        sx -= 1
    if keys [pygame.K_s]:
        sy += 1
    if keys [pygame.K_w]:
        sy -= 1
    
    pygame.display.update()
    
    
