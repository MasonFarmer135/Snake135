import sys
import pygame

#Pygame.
pygame.init()

#Application window settings.
WINDOW_SIZE = 720
resolution = (WINDOW_SIZE,WINDOW_SIZE)
pygame.display.set_caption("Snake135")
window = pygame.display.set_mode(resolution)
windowWidth = window.get_width()
windowHeight = window.get_height()
windowClock = pygame.time.Clock()
windowDisplay = 1

#Variables
userInput = "NONE"
GRID_SIZE = 24
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
debugging = False
#Font
font1 = pygame.font.SysFont("arcade classic", 50, bold = False)

#Text
##Main Menu
mainMenuText1 = font1.render('Click the "Enter" key.', True, ("#FFFFFF"))
mainMenuText1Center = mainMenuText1.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))

#Game
gameText1 = font1.render('Click an "Arrow" key.', True, ("#FFFFFF"))
gameText1Center = gameText1.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
gameText2 = font1.render('', True, ("#FFFFFF"))
gameText2Center = gameText2.get_rect(center = (windowWidth / 2, windowHeight / 2))

#Main Application
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()

        #Main menu
        if (windowDisplay == 1):
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_RETURN):
                    windowDisplay = 2

        #Game
        elif (windowDisplay == 2):
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_UP):
                    userInput = "UP" 
                elif (event.key == pygame.K_DOWN):
                    userInput = "DOWN"
                elif (event.key == pygame.K_LEFT):
                    userInput = "LEFT"
                elif (event.key == pygame.K_RIGHT):
                    userInput = "RIGHT"
                # enable/disable debugging
                elif (event.key == pygame.K_g):
                    debugging = not debugging

    #Main menu
    if (windowDisplay == 1):
        window.fill("#000000")
        window.blit(mainMenuText1, mainMenuText1Center)

    #Game
    if (windowDisplay == 2):
        window.fill("#000000")
        if debugging:
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    gridCell = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(window, (0, 0, 255), gridCell, 1)

        window.blit(gameText1, gameText1Center)
        gameText2 = font1.render(userInput, True, ("#FFFFFF"))
        gameText2Center = gameText2.get_rect(center = (windowWidth / 2, windowHeight / 2))
        window.blit(gameText2, gameText2Center)

    #60 frames per second
    windowClock.tick(60)
    pygame.display.update()
