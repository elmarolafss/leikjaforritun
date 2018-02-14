import pygame
import random
import sys
from pygame import *
pygame.init()



screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)

    return newText


gameDisplay = pygame.display.set_mode((screen_width,screen_height))

white = (255, 255, 255)
black = (0, 0, 0)
gray = (50, 50, 50)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

font = "freesansbold.ttf"
clock = pygame.time.Clock()
FPS = 60
"""""
teningakastari byrjar
"""""
ten1 = pygame.image.load("ten1.png")
ten2 = pygame.image.load("ten2.png")
ten3 = pygame.image.load("ten3.png")
ten4 = pygame.image.load("ten4.png")
ten5 = pygame.image.load("ten5.png")
ten6 = pygame.image.load("ten6.png")
teningalisti = [ten1,ten2,ten3,ten4,ten5,ten6]
def randomten():
    return random.choice(teningalisti)
r1,r2,r3,r4,r5 = (randomten(),randomten(),randomten(),randomten(),randomten())
r11,r22,r33,r44,r55 = (randomten(),randomten(),randomten(),randomten(),randomten())
new = randomten()
mouse = pygame.mouse.get_pos()
def kast2():
    ten1 = 0
    ten2 = 0
    ten3 = 0
    ten4 = 0
    ten5 = 0
    gameDisplay.blit(r11, (screen_width * 0.25, screen_height * 0.5))
    gameDisplay.blit(r22, (screen_width * 0.4, screen_height * 0.5))
    gameDisplay.blit(r33, (screen_width * 0.55, screen_height * 0.5))
    gameDisplay.blit(r44, (screen_width * 0.34, screen_height * 0.3))
    gameDisplay.blit(r55, (screen_width * 0.48, screen_height * 0.3))
    pygame.draw.rect(gameDisplay, black, (220, 450, 100, 50))
    pygame.draw.rect(gameDisplay, black, (400, 450, 100, 50))
    pygame.draw.rect(gameDisplay, red, (320, 450, 100, 50))

    kast = True
    while kast:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            mouse = pygame.mouse.get_pos()
            if 220 + 100 > mouse[0] > 220 and 450 + 50 > mouse[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
                kast2()
            if (screen_width * 0.25) + 100 > mouse[0] > (screen_width * 0.25) and (screen_height * 0.5) + 100 > mouse[1] > (
                    screen_height * 0.5) and event.type == pygame.MOUSEBUTTONDOWN:
                ten1 += 1
                ten2, ten3, ten4, ten5 = 2, 2, 2, 2
            if (screen_width * 0.4) + 100 > mouse[0] > (screen_width * 0.4) and (screen_height * 0.5) + 100 > mouse[1] > (
                    screen_height * 0.5) and event.type == pygame.MOUSEBUTTONDOWN:
                ten2 += 1
                ten1, ten3, ten4, ten5 = 2, 2, 2, 2
            if (screen_width * 0.55) + 100 > mouse[0] > (screen_width * 0.55) and (screen_height * 0.5) + 100 > mouse[1] > (
                    screen_height * 0.5) and event.type == pygame.MOUSEBUTTONDOWN:
                ten3 += 1
                ten1, ten2, ten4, ten5 = 2, 2, 2, 2
            if (screen_width * 0.34) + 100 > mouse[0] > (screen_width * 0.34) and (screen_height * 0.3) + 100 > mouse[1] > (
                    screen_height * 0.3) and event.type == pygame.MOUSEBUTTONDOWN:
                ten4 += 1
                ten1, ten2, ten3, ten5 = 2, 2, 2, 2
            if (screen_width * 0.48) + 100 > mouse[0] > (screen_width * 0.48) and (screen_height * 0.3) + 100 > mouse[1] > (
                    screen_height * 0.3) and event.type == pygame.MOUSEBUTTONDOWN:
                ten5 += 1
                ten1, ten2, ten3, ten4 = 2, 2, 2, 2
            if ten1 == 1 and 320 + 100 > mouse[0] > 320 and 450 + 50 > mouse[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
                gameDisplay.blit(new, (screen_width * 0.25, screen_height * 0.5))
                pygame.draw.rect(gameDisplay, black, (320, 450, 100, 50))
            if ten2 == 1 and 320 + 100 > mouse[0] > 320 and 450 + 50 > mouse[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
                gameDisplay.blit(new, (screen_width * 0.4, screen_height * 0.5))
                pygame.draw.rect(gameDisplay, black, (320, 450, 100, 50))
            if ten3 == 1 and 320 + 100 > mouse[0] > 320 and 450 + 50 > mouse[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
                gameDisplay.blit(new, (screen_width * 0.55, screen_height * 0.5))
                pygame.draw.rect(gameDisplay, black, (320, 450, 100, 50))
            if ten4 == 1 and 320 + 100 > mouse[0] > 320 and 450 + 50 > mouse[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
                gameDisplay.blit(new, (screen_width * 0.34, screen_height * 0.3))
                pygame.draw.rect(gameDisplay, black, (320, 450, 100, 50))
            if ten5 == 1 and 320 + 100 > mouse[0] > 320 and 450 + 50 > mouse[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
                gameDisplay.blit(new, (screen_width * 0.48, screen_height * 0.3))
                pygame.draw.rect(gameDisplay, black, (320, 450, 100, 50))
        pygame.display.update()

def kast():
    kast = True
    ten1 = 0
    ten2 = 0
    ten3 = 0
    ten4 = 0
    ten5 = 0
    pygame.draw.rect(gameDisplay, black, (350, 250, 100, 50))
    gameDisplay.blit(r1, (screen_width * 0.25, screen_height * 0.5))
    gameDisplay.blit(r2, (screen_width * 0.4, screen_height * 0.5))
    gameDisplay.blit(r3, (screen_width * 0.55, screen_height * 0.5))
    gameDisplay.blit(r4, (screen_width * 0.34, screen_height * 0.3))
    gameDisplay.blit(r5, (screen_width * 0.48, screen_height * 0.3))
    pygame.draw.rect(gameDisplay, green, (220, 450, 100, 50))
    pygame.draw.rect(gameDisplay, red, (400, 450, 100, 50))
    while kast:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            mouse = pygame.mouse.get_pos()
            if 220 + 100 > mouse[0] > 220 and 450 + 50 > mouse[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
                kast2()
            if (screen_width * 0.25) + 100 > mouse[0] > (screen_width * 0.25) and (screen_height * 0.5) + 100 > mouse[1] > (screen_height * 0.5) and event.type == pygame.MOUSEBUTTONDOWN:
                ten1 += 1
                ten2,ten3,ten4,ten5 = 2,2,2,2
            if (screen_width * 0.4) + 100 > mouse[0] > (screen_width * 0.4) and (screen_height * 0.5) + 100 > mouse[1] > (screen_height * 0.5) and event.type == pygame.MOUSEBUTTONDOWN:
                ten2 += 1
                ten1,ten3,ten4,ten5 = 2,2,2,2
            if (screen_width * 0.55) + 100 > mouse[0] > (screen_width * 0.55) and (screen_height * 0.5) + 100 > mouse[1] > (screen_height * 0.5) and event.type == pygame.MOUSEBUTTONDOWN:
                ten3 += 1
                ten1,ten2,ten4,ten5 = 2,2,2,2
            if (screen_width * 0.34) + 100 > mouse[0] > (screen_width * 0.34) and (screen_height * 0.3) + 100 > mouse[1] > (screen_height * 0.3) and event.type == pygame.MOUSEBUTTONDOWN:
                ten4 += 1
                ten1,ten2,ten3,ten5 = 2,2,2,2
            if (screen_width * 0.48) + 100 > mouse[0] > (screen_width * 0.48) and (screen_height * 0.3) + 100 > mouse[1] > (screen_height * 0.3) and event.type == pygame.MOUSEBUTTONDOWN:
                ten5 += 1
                ten1,ten2,ten3,ten4 = 2,2,2,2
            if ten1 == 1 and 400 + 100 > mouse[0] > 400 and 450 + 50 > mouse[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
                gameDisplay.blit(new, (screen_width * 0.25, screen_height * 0.5))
            if ten2 == 1 and 400 + 100 > mouse[0] > 400 and 450 + 50 > mouse[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
                gameDisplay.blit(new, (screen_width * 0.4, screen_height * 0.5))
            if ten3 == 1 and 400 + 100 > mouse[0] > 400 and 450 + 50 > mouse[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
                gameDisplay.blit(new, (screen_width * 0.55, screen_height * 0.5))
            if ten4 == 1 and 400 + 100 > mouse[0] > 400 and 450 + 50 > mouse[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
                gameDisplay.blit(new, (screen_width * 0.34, screen_height * 0.3))
            if ten5 == 1 and 400 + 100 > mouse[0] > 400 and 450 + 50 > mouse[1] > 450 and event.type == pygame.MOUSEBUTTONDOWN:
                gameDisplay.blit(new, (screen_width * 0.48, screen_height * 0.3))
        pygame.display.update()
def tening():
    teningur = True
    while teningur:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu()
            if 320 + 100 > mouse[0] > 320 and 250 + 50 > mouse[1] > 250 and event.type == pygame.MOUSEBUTTONDOWN:
                kast()
        mouse = pygame.mouse.get_pos()
        screen.fill(black)
        pygame.draw.rect(gameDisplay, green, (350, 250, 100, 50))

        pygame.display.update()
        clock.tick(FPS)
    return "tening"
"""""
teningakastsri endar
"""""
"""""
safnari byrjar
"""""
def safnari(w):
    safnari = True
    while safnari:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu()
            screen.fill(black)
            text = text_format(w, font, 40, white)
            start = text_format("Press space to start", font, 60, white)

            start_rect = start.get_rect()
            text_rect = text.get_rect()
            screen.blit(start, (screen_width / 2 - (start_rect[2] / 2), 80))
            screen.blit(text, (screen_width / 2 - (text_rect[2] / 2), 190))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    the_collector()
            pygame.display.update()
            clock.tick(FPS)


def object(x,w):
    pygame.draw.rect(gameDisplay, white, (x, 520, w, 15))

def things(thingx, thingy, color):

    gameDisplay.blit(color, (thingx, thingy))

def the_collector():
    counter = 0
    c2 = 0
    collect = True
    x = 350
    w = 100
    x_change = 0

    thing_startx = random.randrange(0, screen_width)
    thing_starty = 0
    thing_speed = 4

    loftsteinn = pygame.image.load("loftsteinn.png")
    stars = pygame.image.load("stars.png")

    while collect:
        for event in pygame.event.get():

            thing_speed += 1
            if event.type == pygame.QUIT:
                main_menu()


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0



        gameDisplay.blit(stars, (0, 0))

        things(thing_startx, thing_starty, loftsteinn)
        thing_starty += thing_speed
        if thing_starty > screen_height:
            thing_starty = 0
            thing_startx = random.randrange(0, screen_width)


        x += x_change

        if thing_starty >= 500 and thing_starty <= 520 and thing_startx <= x + w:
            w += 10
            counter += 1
        if thing_starty >= 525 and thing_starty <= 540:
            c2 += 1
        print(c2)
        if c2 == 20:
            safnari("You Lost :(")
        if counter == 20:
            safnari("You Won!!")
        object(x,w)
        score = text_format("points = %s" % counter, font, 20, white)
        score_rect = score.get_rect()
        screen.blit(score, (screen_width / 2 - (score_rect[2] / 3), 80))
        pygame.display.update()
        clock.tick(FPS)
"""
Safnari endar
"""
"""
Pong byrjar
"""

BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
ball_pos = [0,0]
ball_vel = [0,0]
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0

window = pygame.display.set_mode((screen_width, screen_height), 0, 32)

def ball(right):
    global ball_pos,ball_vel
    ball_pos = [screen_width//2,screen_height//2]
    horizontal = random.randrange(2,4)
    vertical = random.randrange(2,4)

    if right == False:
        horizontal = - horizontal
    ball_vel = [horizontal,-vertical]

def init():
    global paddle1_pos,paddle2_pos,paddle1_vel,paddle2_vel,l_score,r_score
    global score1,score2
    paddle1_pos = [HALF_PAD_WIDTH -1,screen_height//2]
    paddle2_pos = [screen_width +1 - HALF_PAD_WIDTH,screen_height//2]
    l_score = 0
    r_score = 0
    if random.randrange(0,2) == 0:
        ball(True)
    else:
        ball(False)

def draw(canvas):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, l_score, r_score

    canvas.fill(black)
    pygame.draw.line(canvas, white, [screen_width // 2, 0], [screen_width // 2, screen_height], 1)
    pygame.draw.line(canvas, white, [PAD_WIDTH, 0], [PAD_WIDTH, screen_height], 1)
    pygame.draw.line(canvas, white, [screen_width - PAD_WIDTH, 0], [screen_width - PAD_WIDTH, screen_height], 1)



    if paddle1_pos[1] > HALF_PAD_HEIGHT and paddle1_pos[1] < screen_height - HALF_PAD_HEIGHT:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == HALF_PAD_HEIGHT and paddle1_vel > 0:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == screen_height - HALF_PAD_HEIGHT and paddle1_vel < 0:
        paddle1_pos[1] += paddle1_vel

    if paddle2_pos[1] > HALF_PAD_HEIGHT and paddle2_pos[1] < screen_height - HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HALF_PAD_HEIGHT and paddle2_vel > 0:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == screen_height - HALF_PAD_HEIGHT and paddle2_vel < 0:
        paddle2_pos[1] += paddle2_vel


    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])

    pygame.draw.circle(canvas, white, ball_pos, 20, 0)
    pygame.draw.polygon(canvas, white, [[paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT],
                                        [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT],
                                        [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT],
                                        [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT]], 0)
    pygame.draw.polygon(canvas, white, [[paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT],
                                        [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT],
                                        [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT],
                                        [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT]], 0)


    if int(ball_pos[1]) <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if int(ball_pos[1]) >= screen_height + 1 - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]


    if int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH and int(ball_pos[1]) in range(paddle1_pos[1] - HALF_PAD_HEIGHT, paddle1_pos[1] + HALF_PAD_HEIGHT, 1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif int(ball_pos[0]) <= BALL_RADIUS + PAD_WIDTH:
        r_score += 1
        ball(True)

    if int(ball_pos[0]) >= screen_width + 1 - BALL_RADIUS - PAD_WIDTH and int(ball_pos[1]) in range(
            paddle2_pos[1] - HALF_PAD_HEIGHT, paddle2_pos[1] + HALF_PAD_HEIGHT, 1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif int(ball_pos[0]) >= screen_width + 1 - BALL_RADIUS - PAD_WIDTH:
        l_score += 1
        ball(False)


    myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
    label1 = myfont1.render("Score " + str(l_score), 1, (255, 255, 0))
    canvas.blit(label1, (50, 20))

    myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
    label2 = myfont2.render("Score " + str(r_score), 1, (255, 255, 0))
    canvas.blit(label2, (470, 20))


def keydown(event):
    global paddle1_vel, paddle2_vel

    if event.key == K_UP:
        paddle2_vel = -8
    elif event.key == K_DOWN:
        paddle2_vel = 8
    elif event.key == K_w:
        paddle1_vel = -8
    elif event.key == K_s:
        paddle1_vel = 8

def keyup(event):
    global paddle1_vel, paddle2_vel

    if event.key in (K_w, K_s):
        paddle1_vel = 0
    elif event.key in (K_UP, K_DOWN):
        paddle2_vel = 0

def pong():

    init()
    while True:

        draw(window)
        for event in pygame.event.get():

            if event.type == KEYDOWN:
                keydown(event)
            elif event.type == KEYUP:
                keyup(event)
            elif event.type == QUIT:
                main_menu()

        pygame.display.update()
        clock.tick(FPS)




def main_menu():
    menu = True
    selected = "tening"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = "tening"
                elif event.key == pygame.K_LEFT:
                    selected = "safn"
                elif event.key == pygame.K_RIGHT:
                    selected = "pong"
                elif event.key == pygame.K_DOWN:
                    selected = "quit"
                if event.key == pygame.K_RETURN:
                    if selected == "tening":
                        menu = False
                        print(tening())
                    if selected == "safn":
                        safnari("Reach 20 points!")
                    if selected == "pong":
                        pong()
                    if selected == "quit":
                        pygame.quit()
                        quit()


        screen.fill(blue)
        title = text_format("Verkefni 1", font, 90, black)
        if selected == "tening":
            text_tening = text_format("Teningakastarinn", font, 65, white)
        else:
            text_tening = text_format("Teningakastarinn", font, 60, black)
        if selected == "safn":
            text_safn = text_format("Safnarinn", font, 65, white)
        else:
            text_safn = text_format("Safnarinn", font, 60, black)
        if selected == "pong":
            text_pong = text_format("Pong", font, 65, white)
        else:
            text_pong = text_format("Pong", font, 60, black)
        if selected == "quit":
            text_quit = text_format("QUIT", font, 65, white)
        else:
            text_quit = text_format("QUIT", font, 60, black)

        title_rect = title.get_rect()
        tening_rect = text_tening.get_rect()
        safn_rect = text_safn.get_rect()
        pong_rect = text_pong.get_rect()
        quit_rect = text_quit.get_rect()

        screen.blit(title, (screen_width / 2 - (title_rect[2] / 2), 80))
        screen.blit(text_tening, (screen_width / 2 - (tening_rect[2] / 2), 180))
        screen.blit(text_safn, (screen_width / 4 - (safn_rect[2] / 2), 250))
        screen.blit(text_pong, (screen_width * 0.7- (pong_rect[2] / 2), 250))
        screen.blit(text_quit, (screen_width / 2 - (quit_rect[2] / 2), 300))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Verkefni 1")

main_menu()
pygame.quit()
quit()
