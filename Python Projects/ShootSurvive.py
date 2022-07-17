import random

import pygame

pygame.init()

# SCREEN INFO/SETTINGS
screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("Title for your Game")
icon = pygame.image.load('bun.jpg')
pygame.display.set_icon(icon)

# PLAYER INFO
playerimg = pygame.image.load('Actor.png')
playerX = int(800)
playerY = int(420)
playerXchange = int(0)
playerYchange = int(0)

def player(x, y):
    screen.blit(playerimg, (x, y))


# ENEMY INFO
enemyimg = pygame.image.load('enemy.png')
enemyX = int(random.randint(0, 1550))
enemyY = int(random.randint(0, 835))
enemyXchange = .2
enemyYchange = .2

def enemy(x, y):
    screen.blit(enemyimg, (x, y))


# BULLET INFO
bulletimg = pygame.image.load('bullet.png')
bulletX = playerX
bulletY = playerY
bulletXchange = int(3)
bulletYchange = int(3)
bulletstate = "ready"

def fire_bullet(x, y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletimg, (x, y))


# THIS MAKES EVERYTHING RUN; YOU NEED TO PUT CODE IN THIS WHILE LOOP ANYTHING TO HAPPEN WITHIN THE GAME.
# THIS IS WHERE THE GAME STARTS.
game_on = True
while game_on:
    screen.fill((0, 0, 0))  # THIS PART OF THE CODE LETS YOUR SPRITES NOT HAVE FUCKIN TRAILS FOREVER!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:  # THIS PART DOES THE KEYBOARD COMMANDS FOR WASD.
            if event.key == pygame.K_a:
                playerXchange = - 0.5
            if event.key == pygame.K_d:
                playerXchange = 0.5
            if event.key == pygame.K_w:
                playerYchange = - 0.5
            if event.key == pygame.K_s:
                playerYchange = 0.5
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, playerY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerXchange = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerYchange = 0

    playerX += playerXchange  # 800 = 800 + -0.5 -> 800 = 800 - 0.5 ALSO 800 + 0.5
    playerY += playerYchange  # 420 = 420 + -0.5 -> 420 = 420 - 0.5 ALSO 420 + 0.5

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1550:  # THIS PART OF THE CODE ADDS THE BORDERS FOR THE PLAYER.
        playerX = 1550  # IT'S FOR BOTH THE Y AND X COORDINATES TO UTILIZE FULL MOVEMENT IN THE WINDOW.
    if playerY <= 0:
        playerY = 0
    elif playerY >= 835:
        playerY = 835

    enemyX += enemyXchange
    enemyY += enemyYchange

    if enemyX <= 0:
        enemyXchange = 0.2
    elif enemyX >= 1550:  # THIS PART OF THE CODE ADDS THE BORDERS FOR THE ENEMY....IN THEORY....
        enemyXchange = -0.2  # I MAY WANT TO GET RID OF THIS PART OF THE CODE HONESTLY, BUT IT WORKS FOR NOW.
    if enemyY <= 0:  # BECAUSE I MIGHT WANT ENEMIES TO COME FROM OFFSCREEN AND GO TOWARDS THE PLAYER.
        enemyYchange = 0.2
    elif enemyY >= 835:
        enemyYchange = -0.2

    # BULLET MOVEMENT......I STILL HAVENT TOTALLY FIGURED THIS SHIT OUT
    if bulletstate == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY += bulletYchange
        bulletX += bulletXchange

    enemy(enemyX, enemyY)
    player(playerX, playerY)
    pygame.display.update()
