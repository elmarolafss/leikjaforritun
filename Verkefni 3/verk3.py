from pygame import *
import random

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.map = image.load(filename)
        self.map.set_colorkey((0,0,0))
    def set_position(self,xpos,ypos):
        self.x = xpos
        self.y = ypos
    def render(self):
        screen.blit(self.map, (self.x, self.y))

def Intersect(sp1_x, sp1_y, sp2_x, sp2_y):
    if (sp1_x > sp2_x - 35) and (sp1_x < sp2_x + 32) and (sp1_y > sp2_y - 32) and (sp1_y < sp2_y + 32):
        return 1
    else:
        return 0

init()
screen = display.set_mode((640, 480))
key.set_repeat(1, 1)
display.set_caption("Verkefni 3")
backdrop = image.load("pic/bc.png")

enemies = []
lives = []

x = 0
for count in range(10):
    enemies.append(Sprite(50 * x + 50, 50,"pic/enemy.png"))
    x += 1
x = 0
for count in range(5):
    lives.append(Sprite(50 * x + 390,20, "pic/heart.png"))
    x += 1

me = Sprite(20,400,"pic/me.png")
meMissile = Sprite(0,480, "pic/missile.png")
enemyMissile = Sprite(0,480, "pic/enemyMissile.png")

quit = 0
enemyspeed = 3

x = 0
while quit == 0:

    screen.blit(backdrop, (0,0))
    for count in range(len(enemies)):
        enemies[count].x += enemyspeed
        enemies[count].render()

    for count in range(len(lives)):
        lives[count].render()

    if enemies[len(enemies) - 1].x > 590:
        enemyspeed = -3
        for count in range(len(enemies)):
            enemies[count].y += 5

    if enemies[0].x < 10:
        enemyspeed = 3
        for count in range(len(enemies)):
            enemies[count].y += 5

    if meMissile.y < 479 and meMissile.y > 0:
        meMissile.render()
        meMissile.y += -5

    if enemyMissile.y >= 480 and len(enemies) > 0:
        enemyMissile.x = enemies[random.randint(0, len(enemies) - 1)].x
        enemyMissile.y = enemies[0].y



    if Intersect(me.x, me.y, enemyMissile.x, enemyMissile.y,):
        x+=1
        print(x)
        if x == 1:
            del lives[0]
        if x == 20:
            del lives[0]
        if x == 30:
            del lives[0]
        if x == 40:
            del lives[0]
        if x == 50:
            del lives[0]

    for count in range(0, len(enemies)):
        if Intersect(meMissile.x, meMissile.y, enemies[count].x, enemies[count].y):
            del enemies[count]
            break

    if len(lives) == 0:
        print("dieded")
        quit+=1

    if len(enemies) == 0:
        print("win")
        quit+=1

    for ourevent in event.get():
        if ourevent.type == QUIT:
            quit = 1
        if ourevent.type == KEYDOWN:
            if ourevent.key == K_RIGHT and me.x < 615:
                me.x += 5
            if ourevent.key == K_LEFT and me.x > 0:
                me.x -= 5
            if ourevent.key == K_UP and me.y > 5:
                me.y -= 5
            if ourevent.key == K_DOWN and me.y < 435:
                me.y += 5
            if ourevent.key == K_SPACE:
                meMissile.x = me.x
                meMissile.y = me.y

    enemyMissile.render()
    enemyMissile.y += 5

    me.render()

    display.update()
    time.delay(5)