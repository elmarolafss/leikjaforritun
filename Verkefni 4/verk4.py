import pygame
from pygame import *
pygame.init()

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

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

lives = []
lives2 = []

size = (1200,800)
key.set_repeat(1, 1)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tanks")
tank1 = Sprite(1030,10,"pic/greenship3.png")
tank2 = Sprite(30,600,"pic/greenship4.png")
background = image.load("pic/trees-and-bushes.png")
enemyMissile = Sprite(0,480, "pic/enemyMissile.png")
meMissile = Sprite(10,480, "pic/missile.png")

for x in range(5):
    lives.append(Sprite(50 * x + 5, 5, "pic/heart.png"))
for x in range(5):
    lives2.append(Sprite(50 * x + 950, 750, "pic/heart.png"))

carryOn = True

clock = pygame.time.Clock()
hit=0
hit2=0
while carryOn:
    for event in pygame.event.get():
        if event.type == QUIT:
            carryOn = False

    keys = pygame.key.get_pressed()
    if keys[K_RIGHT] and tank2.x < 1080:
        tank2.x += 20
    if keys[K_LEFT] and tank2.x > 0:
        tank2.x -= 20
    if keys[K_UP] and tank2.y > 0:
        tank2.y -= 20
    if keys[K_DOWN] and tank2.y < 600:
        tank2.y += 20
    if keys[K_KP_ENTER]:
        enemyMissile.x = tank2.x + 50
        enemyMissile.y = tank2.y
    if keys[K_d] and tank1.x < 1080:
        tank1.x += 20
    if keys[K_a] and tank1.x > 0:
        tank1.x -= 20
    if keys[K_w] and tank1.y > 0:
        tank1.y -= 20
    if keys[K_s] and tank1.y < 600:
        tank1.y += 20
    if keys[K_SPACE]:
        meMissile.x = tank1.x + 50
        meMissile.y = tank1.y + 200

        # --- Game logic should go here

        # --- Drawing code should go here

    x = 0
    y = 0
    for i in range(5):
        screen.blit(background,(x,y))
        x+=280
    x=0
    for i in range(5):
        screen.blit(background,(x,y))
        y+=160
    y=0
    for i in range(5):
        screen.blit(background,(280,y))
        y += 160
    y=0
    for i in range(5):
        screen.blit(background,(560,y))
        y += 160
    y=0
    for i in range(5):
        screen.blit(background,(840,y))
        y += 160
    y=0
    for i in range(5):
        screen.blit(background,(1120,y))
        y += 160


    meMissile.render()
    meMissile.y += 20

    enemyMissile.render()
    enemyMissile.y -= 20

    if Intersect(tank1.x, tank1.y, enemyMissile.x, enemyMissile.y,):
        hit+=1
        print(hit)
        if hit == 1:
            del lives[0]
        if hit == 5:
            del lives[0]
        if hit == 10:
            del lives[0]
        if hit == 15:
            del lives[0]
        if hit == 20:
            del lives[0]
    if Intersect(tank2.x, tank2.y, meMissile.x, meMissile.y, ):
        hit2 += 1
        print(hit2)
        if hit2 == 1:
            del lives2[0]
        if hit2 == 5:
            del lives2[0]
        if hit2 == 10:
            del lives2[0]
        if hit2 == 15:
            del lives2[0]
        if hit2 == 20:
            del lives2[0]

    for count in range(len(lives)):
        lives[count].render()
    for count in range(len(lives2)):
        lives2[count].render()
    for i in lives:
        if i == 0:
            print("player2wins")
    if lives2 == 0:
        print("Player1wins")

    tank1.render()
    tank2.render()
    pygame.display.update()


    clock.tick(60)

pygame.quit()