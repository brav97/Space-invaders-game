import pygame
pygame.init()
import random
import math

screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load('background.png')

#game name and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('transport.png')
pygame.display.set_icon(icon)

#players
playerImg = pygame.image.load( 'spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyImg = pygame.image.load( 'transportation.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(30, 150)
enemyX_change = 3
enemyY_change = 60

#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 10
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'

score_value = 0
font= pygame.font.Font ('freesansbold.ttf', 32)
textX = 10
textY = 10


def show_score( X, Y):
        score = font.render('score : ' + str(score_value), True, (0, 128, 128))
        screen.blit(score, (X, Y))

def enemy( enemyX, enemyY):
    screen.blit( enemyImg, (enemyX, enemyY))

def player( playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))

def fire_bullet ( bulletX, bulletY):
    global bullet_state
    bullet_state = 'fire'
    screen.blit (bulletImg, (bulletX + 17, bulletY + 11))

def isCollision (enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt ((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False


#game loop
running = True
while running:

#screen colors
    screen.fill((0, 0, 0))
    screen.blit(background, (0,0))
    playerX -= 0.1



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #check if key is pressed
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736
  



    enemyX += enemyX_change
    if enemyX <=0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change


    #bullet movement
    if bulletY <= 0:
        bulletY =  480
        bullet_state = 'ready'

    if bullet_state is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state ='ready'
        score_value += 1

        enemyY =random.randint(0,350)
        enemyX = random.randint (0, 150)

    player(playerX, playerY)
    enemy( enemyX, enemyY)
    show_score(textX, textY)
    pygame.display.update()
