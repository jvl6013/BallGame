#Basic setup
import pygame
import math

pygame.init()

#RGB
BLACK = [0, 0, 0]

#Variable
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WINDOW_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]

screen = pygame.display.set_mode(WINDOW_SIZE)

done = False

clock = pygame.time.Clock()

characterImg = pygame.image.load('macman.png')

def character(x, y, image):
    screen.blit(image, (x, y))

right = False
left = False
jump = False
down = False

x = SCREEN_WIDTH/3
y = SCREEN_HEIGHT - 20

gravity = 1
jumpHeight = 50
time = math.sqrt(jumpHeight * 2)

 #Background
bkgd = pygame.image.load("background.png").convert()
bkgd_x = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # KEYBOARD INPUT
        if event.type == pygame.KEYDOWN:
            '''            
            if event.key == pygame.K_RIGHT:
                print("on")
                right = True;
            if event.key == pygame.K_LEFT:
                left = True;
            '''
            if event.key == pygame.K_SPACE:
                print("on")
                jump = True;

        if event.type == pygame.KEYUP:
            '''
            if event.key == pygame.K_RIGHT:
                print("off")
                right = False
            if event.key == pygame.K_LEFT:
                left = False
            '''

    if right:
        x += 5
    if left:
        x -= 5


    if jump:
        if(y > 500 and down is False):
            y -= 7
        elif(y < 580 and down is True):
            print("DOwn")
            y += 7
            if(y == 580):
                jump = False
                down = False
        else:
            down = True

        print(down)

    print(y)



    screen.blit(bkgd, (bkgd_x, 0) )

    #screen.fill(BLACK)

    character(x, y, characterImg)

    clock.tick(60)
    pygame.display.flip()


pygame.quit()




