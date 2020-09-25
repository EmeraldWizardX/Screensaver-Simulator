import pygame
from pygame import mixer
from MainMenu import MainMenu
import os
def create_window(color):
    screen = pygame.display.set_mode((800, 800))
    screen.fill(color)
    pygame.display.set_caption('Screensaver Simulator')
    return screen

def main():
    main = MainMenu()
    main.draw_Window()
    # Grab Background from MainMenu.py
    if main.bg == "Forest":
        Background = pygame.image.load("ForestBackround.jpg")
    elif main.bg == "Sky":
        Background = pygame.image.load("SkyBackground.jpeg")
    elif main.bg == "Mountian":
        Background = pygame.image.load("MountiansBackground.jpg")
    elif main.bg == "Beach":
        Background = pygame.image.load("BeachBackground.jpg")
    else:
        Background = pygame.image.load("PlaceHolderBackground.png")
    Background = pygame.transform.scale(Background, (800, 800))
    # Grab Icon from MainMenu.py
    if main.icon == "Squarey":
        Icon = pygame.image.load("Squarey.jpg")
    elif main.icon == "DVD Video":
        Icon = pygame.image.load("dvdBlue.png")
    elif main.icon == "Minecraft Grass Block":
        Icon = pygame.image.load("GRASS.jpg")
    elif main.icon == "Upload Image":
        Icon = pygame.image.load('BaseImage.png')
    elif main.icon == "Python Logo":
        Icon = pygame.image.load("PythonLogoBoxed.png")
    else:
        Icon = pygame.image.load("PlaceHolderTexture.png")
    icon = pygame.transform.scale(Icon, (100, 100))
    # Initialize Music
    mixer.init()
    mixer.music.load('Kevin MacLeod Winner Winner!.wav')
    mixer.music.play(-1)
    pygame.init()
    clock = pygame.time.Clock()

    BLACK = (0, 0, 0)
    # create window
    screen = create_window(BLACK)

    # x and y vars
    XCOR = 300
    YCOR = 302

    CHANGE_X = 2
    CHANGE_Y = 3

    # start game loop
    done = False
    while not done:
        screen.fill(BLACK)
        screen.blit(Background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            keys = pygame.key.get_pressed()
            for key in keys:
                if keys[pygame.K_ESCAPE]:
                    done = True

        # draw the image
        screen.blit(icon, (XCOR, YCOR))

        # update location
        if XCOR < 0 or XCOR > 700:
            CHANGE_X = -CHANGE_X
        # y cordinate check
        if YCOR < 0 or YCOR > 700:
            CHANGE_Y = -CHANGE_Y

        # update values
        XCOR = XCOR + CHANGE_X
        YCOR = YCOR + CHANGE_Y
        # update screen
        pygame.display.update()
        clock.tick(30)


pygame.quit()  # MUST DO
main()
