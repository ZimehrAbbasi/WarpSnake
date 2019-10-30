import pygame
import random
import numpy as np

pygame.init()

win = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Snake")
myfont = pygame.font.SysFont("monospace", 15)

cpu_sound = pygame.mixer.Sound("Soundeffects/cpu.wav")
ct_sound = pygame.mixer.Sound("Soundeffects/ct.wav")
hnsm_sound = pygame.mixer.Sound("Soundeffects/HNSM.wav")

x = 20
y = 20
width = 10
height = 10
xv = 10
yv = 0

locx = 100
locy = 100

score = 0
i = 0
_snake = np.array([pygame.draw.rect(win, (237, 237, 237), (x, y, width, height))])
path = [[x, y, xv, yv]]

def _quit():
    pygame.quit()
    quit()

run = True
while run:
    pygame.time.delay(100)

    x = x + xv
    y = y + yv

    path.insert(0, [x, y, xv, yv])
    _path = np.array(path)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 10:
        if xv != 10:
            xv = -10
            yv = 0

    if keys[pygame.K_RIGHT] and x < 291:
        if xv != -10:
            xv = 10
            yv = 0

    if keys[pygame.K_UP] and y < 291:
        if yv != 10:
            yv = -10
            xv = 0

    if keys[pygame.K_DOWN] and y > 10:
        if yv != -10:
            yv = 10
            xv = 0

    if x > 285:
        xv = 0
        yv = 0

        _quit()
    elif x < 10:
        xv = 0
        yv = 0

        _quit()
    elif y > 285:
        xv = 0
        yv = 0

        _quit()
    elif y < 20:
        xv = 0
        yv = 0

        _quit()

    win.fill((19, 20, 25))

    i = 0
    for i in range(score+1):
        if xv > 0:
            _snake = np.insert(_snake, 0, pygame.draw.rect(win, (237, 237, 237), ((int(_path[i, 0]) + int(_path[i, 2])), (int(_path[i, 1]) + int(_path[i, 3])), width, height)))
        elif xv < 0:
            _snake = np.insert(_snake, 0, pygame.draw.rect(win, (237, 237, 237), ((int(_path[i, 0]) + int(_path[i, 2])), (int(_path[i, 1]) + int(_path[i, 3])), width, height)))
        elif yv > 0:
            _snake = np.insert(_snake, 0, pygame.draw.rect(win, (237, 237, 237), ((int(_path[i, 0]) + int(_path[i, 2])), (int(_path[i, 1]) + int(_path[i, 3])), width, height)))
        elif yv < 0:
            _snake = np.insert(_snake, 0, pygame.draw.rect(win, (237, 237, 237), ((int(_path[i, 0]) + int(_path[i, 2])), (int(_path[i, 1]) + int(_path[i, 3])), width, height)))
        i += 1

    _food = pygame.draw.rect(win, (195, 7, 63), (locx, locy, 10, 10))

    n_w = 0
    while n_w in range(30):
        pygame.draw.rect(win, (0, 0, 0), (10 * n_w, 10, 10, 10))
        n_w += 1

    n_w1 = 0
    while n_w1 in range(30):
        pygame.draw.rect(win, (0, 0, 0), (10 * n_w1, 290, 10, 10))
        n_w1 += 1

    n_w2 = 0
    while n_w2 in range(30):
        pygame.draw.rect(win, (0, 0, 0), (0, 10 * n_w2, 10, 10))
        n_w2 += 1

    n_w3 = 0
    while n_w3 in range(30):
        pygame.draw.rect(win, (0, 0, 0), (290, 10 * n_w3, 10, 10))
        n_w3 += 1

    n_w4 = 0
    while n_w4 in range(30):
        pygame.draw.rect(win, (0, 0, 0), (10 * n_w4, 0, 10, 10))
        n_w4 += 1

    m = 2

    for m in range(score):
        if score > 3:
            if _snake[0] == (int(_path[m, 0]) + int(_path[m, 2])) and _snake[1] == (int(_path[m, 1]) + int(_path[m, 3])):
                _quit()


    if x == locx and y == locy:
        locx = 10 * random.randint(2, 27)
        locy = 10 * random.randint(3, 27)
        score += 1

        if score == 10:
            pygame.mixer.Sound.play(ct_sound)
            pygame.mixer.music.stop()
        elif score == 20:
            pygame.mixer.Sound.play(hnsm_sound)
            pygame.mixer.music.stop()
        elif score > 20 and score % 10 == 0:
            pygame.mixer.Sound.play(ct_sound)
            pygame.mixer.music.stop()
        else:
            pygame.mixer.Sound.play(cpu_sound)
            pygame.mixer.music.stop()

    label = myfont.render("Score: " + str(score), 1, (255, 255, 0))
    win.blit(label, (130, 0))

    pygame.display.update()



_quit()
