#Basic setup
from random import randint

import pygame
import math

pygame.init()

clock = pygame.time.Clock()

#RGB
BLACK = [0, 0, 0]
GRAY = [170, 170, 170]
RED = [255, 0, 0]
WHITE = [255, 255, 255]
GREEN = [0, 168, 0]
LIGHT_GREEN = [0, 200, 0]
DARKGRAY = [100, 100, 100]
CYAN = [66, 241, 244]

#FONT
score_font = pygame.font.SysFont('Arial', 15)

#Variable
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WINDOW_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
LIFE = 3
JUMP_HOLD = 0;
SCORE_COUNTER = 0;
SCORE = 0;

screen = pygame.display.set_mode(WINDOW_SIZE)

#SPRITE CLASSSES

class HealthPack(pygame.sprite.Sprite):
    def __init__(self):
        hp_height = randint(280, 320)
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((24, 24), pygame.SRCALPHA)
        pygame.draw.rect(self.image, RED, (0, 8, 24, 8))
        pygame.draw.rect(self.image, RED, (8, 0, 8, 24))
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = hp_height

    def update(self):
        self.rect.x -= 2
        if(self.rect.x <= -25):
            self.__init__()

    def disappear(self):
        self.image = pygame.Surface((0,0), pygame.SRCALPHA)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.obs_height = randint(100, 400)
        self.ball_gravity = 5
        self.ball_size = randint(1, 4)

        if(self.ball_size == 1):
            self.ball_size = 14
        elif(self.ball_size == 2):
            self.ball_size = 16
        elif (self.ball_size == 3):
            self.ball_size = 22
        elif (self.ball_size == 4):
            self.ball_size = 26

        self.image = pygame.Surface((self.ball_size, self.ball_size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, CYAN, (int(self.ball_size/2), int(self.ball_size/2)), int(self.ball_size/2), 0)
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = self.obs_height

    def update(self):
        self.rect.x -= 7
        if(self.rect.y < (SCREEN_HEIGHT - (164 + self.ball_size))):
            self.rect.y += self.ball_gravity
        if(self.rect.x <= -25):
            self.__init__()

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.obs_height = randint(100, 350)
        self.image = pygame.Surface((26, 26))
        self.image.fill(DARKGRAY)
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = self.obs_height

    def update(self):
        self.rect.x -= 5
        if (self.rect.x <= -25):
            self.__init__()

    def getHeight(self):
        return self.obs_height

class Bullet_Head(pygame.sprite.Sprite):
    def __init__(self, bullet_x, bullet_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25, 25), pygame.SRCALPHA)
        pygame.draw.circle(self.image, DARKGRAY, (13, 13), 13, 0)
        self.rect = self.image.get_rect()
        self.rect.x = bullet_x
        self.rect.y = bullet_y

    def update(self):
        self.rect.x -= 5
        if (self.rect.x <= -25):
            self.rect.x = 600

    def setHeight(self, height):
        self.rect.y = height

class Pipe_Top(pygame.sprite.Sprite):
    def __init__(self, pipe_x, pipe_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((31, 5))
        self.image.fill(LIGHT_GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = pipe_x - 3
        self.rect.y = pipe_y - 6

    def update(self):
        self.rect.x -= 3
        if (self.rect.x <= -25):
            self.rect.x = 600

    def setHeight(self, height):
        self.rect.y = height - 6

class Pipe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.obs_height = randint(15, 40)
        self.image = pygame.Surface((25, self.obs_height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = SCREEN_HEIGHT - (162 + self.obs_height)

    def update(self):
        self.rect.x -= 3
        if (self.rect.x <= -25):
            self.__init__()

    def getHeight(self):
        return (SCREEN_HEIGHT - (162 + self.obs_height))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.image.load('ball.png')
        self.image = pygame.Surface((25, 25))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH/2
        self.rect.y = SCREEN_HEIGHT/2
        self.LIFE = 3

    def update(self):
        self.rect.x = player_x
        self.rect.y = player_y
        if(self.LIFE == 0):
            screen.exit()

class Life(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('life.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def lose_life(self):
        self.image = pygame.image.load('life_lost.png')
    def gain_life(self):
        self.image = pygame.image.load('life.png')

#Sprite Group
all_sprites = pygame.sprite.Group()

#Initatilize Sprites
pipe = Pipe()
pipe_top = Pipe_Top(pipe.rect.x, pipe.getHeight())
player = Player()
ball = Ball()
bullet = Bullet()
bullet_head = Bullet_Head(bullet.rect.x - 10, bullet.rect.y)
healthpack = HealthPack()
life1 = Life(SCREEN_WIDTH - (SCREEN_WIDTH - 20), SCREEN_HEIGHT - (SCREEN_HEIGHT - 20))
life2 = Life(SCREEN_WIDTH - (SCREEN_WIDTH - 45), SCREEN_HEIGHT - (SCREEN_HEIGHT - 20))
life3 = Life(SCREEN_WIDTH - (SCREEN_WIDTH - 70), SCREEN_HEIGHT - (SCREEN_HEIGHT - 20))

#Add sprites in a group
all_sprites.add(pipe)
all_sprites.add(pipe_top)
all_sprites.add(bullet_head)
all_sprites.add(bullet)
all_sprites.add(ball)
all_sprites.add(healthpack)
all_sprites.add(life1)
all_sprites.add(life2)
all_sprites.add(life3)
all_sprites.add(player)

collisionCounter = 0
hp_collisionCounter = 0

def checkCollision(player, sprite2, col_counter):
    col = pygame.sprite.collide_rect(player, sprite2)
    if col == True:
        print("Collision Detected")
        player.LIFE -= 1
        print("life = ", player.LIFE)
        col_counter = -60;
        if(player.LIFE == 2):
            life3.lose_life();
        if (player.LIFE == 1):
            life2.lose_life();

    return col_counter

def checkHPCollision(player, sprite2, hp_col_counter):
    col = pygame.sprite.collide_rect(player, sprite2)
    if col == True:
        print("HP Detected")
        healthpack.disappear()
        hp_col_counter = -60;
        if(player.LIFE == 2):
            life3.gain_life();
        elif (player.LIFE == 1):
            life2.gain_life();
        if (player.LIFE < 3):
            player.LIFE += 1
        print("life = ", player.LIFE)
    return hp_col_counter

right = False
left = False
jump = False
down = False

player_x = SCREEN_WIDTH / 3
player_y = SCREEN_HEIGHT - 187

gravity = 1
JUMP_HEIGHT = 100
jump_action = False;
time = math.sqrt(JUMP_HEIGHT * 2)

#Background
bkgd = pygame.image.load("background.png").convert()
bkgd_x = 0

#Game Loop
done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # KEYBOARD INPUT
        if event.type == pygame.KEYDOWN:
            '''            
            if event.key == pygame.K_RIGHT:
                right = True;
            if event.key == pygame.K_LEFT:
                left = True;
            '''
            if event.key == pygame.K_SPACE:
                JUMP_HOLD = 80
                jump = True


        if event.type == pygame.KEYUP:
            '''
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False
            '''
            if event.key == pygame.K_SPACE:
                jump = False
                jump_action = True;

    if right:
        player_x += 5
    if left:
        player_x -= 5

    if jump:
        if(JUMP_HOLD < 140):
            JUMP_HOLD += 2

    if jump_action:
        if (player_y > (SCREEN_HEIGHT - (187 + JUMP_HOLD)) and down is False):
            player_y -= 9
        elif (player_y < (SCREEN_HEIGHT - 187) and down is True):
            player_y += 9
            if (player_y == (SCREEN_HEIGHT - 187)):
                jump_action = False
                down = False
                JUMP_HOLD = 0
        else:
            down = True

    #Rotating Background
    bkgd_rel_x = bkgd_x % (bkgd.get_rect().width)

    screen.blit(bkgd, (bkgd_rel_x - bkgd.get_rect().width, 0))
    if(bkgd_rel_x < SCREEN_WIDTH):
        screen.blit(bkgd, (bkgd_rel_x, 0))

    #Determine Background Rotating Speed
    bkgd_x -= 3;

    #screen.fill(BLACK)

    clock.tick(60)

    all_sprites.draw(screen)

    if(collisionCounter > 0):
        collisionCounter = checkCollision(player, pipe, collisionCounter)
        collisionCounter = checkCollision(player, bullet_head, collisionCounter)
        collisionCounter = checkCollision(player, ball, collisionCounter)

    if(hp_collisionCounter > 0):
        hp_collisionCounter = checkHPCollision(player,healthpack, hp_collisionCounter)

    hp_collisionCounter += 1
    collisionCounter += 1

    #Display Score
    SCORE_COUNTER += 1;
    if(SCORE_COUNTER % 60 == 0):
        SCORE += 1
        print(SCORE)

    score_text = "SCORE: " + str(SCORE)
    score_text = score_text.encode()
    textsurface = score_font.render(score_text, False, WHITE)
    screen.blit(textsurface, (SCREEN_WIDTH - 100, 15))

    #Update the screen every frame
    all_sprites.update()
    pipe_top.setHeight(pipe.getHeight())
    bullet_head.setHeight(bullet.getHeight())
    pygame.display.update()

pygame.quit()





