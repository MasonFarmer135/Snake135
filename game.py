import sys
import pygame

#pygame.
pygame.init()

#Application window settings.
resolution = (800,800)
pygame.display.set_caption("Snake135")
window = pygame.display.set_mode(resolution)
windowWidth = window.get_width()
windowHeight = window.get_height()
windowClock = pygame.time.Clock()

#Main Application
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()

    window.fill("#000000")

    #60 frames per second
    windowClock.tick(60)
    pygame.display.update()
    