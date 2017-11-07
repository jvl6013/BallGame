import pygame
pygame.init()
ferahgasdgswergaefaw
BLACK = [0, 0, 0]

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
WINDOW_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(WINDOW_SIZE)

done = False

clock = pygame.time.Clock()

characterImg = pygame.image.load('macman.png')

def character(x, y, image):
    screen.blit(image, (x, y))

x = SCREEN_WIDTH/2
y = SCREEN_HEIGHT/2

up = y = -10
down = 10

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #KEYBOARD INPUT
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            if(y > 240):
                y -= 10



    screen.fill(BLACK)

    character(x, y, characterImg)

    clock.tick(60)
    pygame.display.flip()


pygame.quit()




