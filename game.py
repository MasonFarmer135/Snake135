import sys
import pygame
import json

#Pygame.
pygame.init()

#Application window settings.
resolutionInfo = pygame.display.Info()
resolution = (resolutionInfo.current_w,resolutionInfo.current_h)

#Less than HD (1280p x 720p)
if (resolution[0] < 1280 and resolution[1] < 720):
    print ("ERROR: This Game is not compatible with this device.")
    deviceCompatibility = False

#HD (1280p x 720p) 
elif ((resolution[0] >= 1280 and resolution[0] < 1920) and (resolution[1] >= 720 and resolution[1] < 1080)):
    #24 x 30 = 730, 24 x 25 = 600 
    WINDOW_SIZE = 600
    deviceCompatibility = True

#FULL HD (1920p x 1080p)
elif ((resolution[0] >= 1920 and resolution[0] < 2560) and (resolution[1] >= 1080 and resolution[1] < 1440)):
    #24 x 45 = 1080, 24 x 40 = 960
    WINDOW_SIZE = 960
    deviceCompatibility = True

#2K (2560p x 1440p)
elif ((resolution[0] >= 2560 and resolution[0] < 3840) and (resolution[1] >= 1440 and resolution[1] < 2160)):
    #24 x 60 = 1440, 24 x 55 = 1320
    WINDOW_SIZE = 1320
    deviceCompatibility = True

#More than 4k (3840p x 2160p)
elif (resolution[0] >= 3840 and resolution[1] >= 2160):
    #24 x 60 = 1440, 24 x 55 = 1320
    WINDOW_SIZE = 1320
    deviceCompatibility = True

resolution = (WINDOW_SIZE,WINDOW_SIZE)
pygame.display.set_caption("Snake135")
window = pygame.display.set_mode(resolution)
windowWidth = window.get_width()
windowHeight = window.get_height()
windowClock = pygame.time.Clock()
windowDisplay = 1

#Variables
userInput = "NONE"
usernameInput = ""
passwordInput = ""
UserID = ""
signInNum = 1
username = ""
password = ""
signIn = False
GRID_SIZE = 24
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
debugging = True

#Font
font1 = pygame.font.SysFont("arcade", 100, bold = False)
font2 = pygame.font.SysFont("arcade", 40, bold = False)

#Text
splashScreenText1 = font1.render("Snake135", True, ("#FFFFFF"))
splashScreenText1Center = splashScreenText1.get_rect(center = (windowWidth / 2, windowHeight / 2 / 2))
splashScreenText2 = font2.render('Click the "Enter" key.', True, ("#FFFFFF"))
splashScreenText2Center = splashScreenText2.get_rect(center = (windowWidth / 2, windowHeight / 2))

loginText1 = font1.render("Sign-in", True, ("#FFFFFF"))
loginText1Center = loginText1.get_rect(center = (windowWidth / 2, windowHeight / 2 / 2))
loginText2 = font1.render("Username: ", True, ("#FFFFFF"))
loginText2Center = loginText2.get_rect(center = (windowWidth / 2, windowHeight / 2))
loginText3 = font1.render("Password: ", True, ("#FFFFFF"))
loginText3Center = loginText3.get_rect(center = (windowWidth / 2, windowHeight / 1.5))


mainMenuText1 = font1.render('Click the "Enter" key.', True, ("#FFFFFF"))
mainMenuText1Center = mainMenuText1.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))

gameText1 = font1.render('Click an "Arrow" key.', True, ("#FFFFFF"))
gameText1Center = gameText1.get_rect(center = (windowWidth / 2, windowHeight / 2 - 200))
gameText2 = font1.render("", True, ("#FFFFFF"))
gameText2Center = gameText2.get_rect(center = (windowWidth / 2, windowHeight / 2))

#Main Application
while True and deviceCompatibility == True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()

        #Splash screen
        if (windowDisplay == 1):
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_RETURN):
                    windowDisplay = 2

        #User account
        elif (windowDisplay == 2):
            if (signIn == False):
                if (signInNum == 1):
                    if (event.type == pygame.KEYDOWN):
                        if (event.key == pygame.K_a) or (event.key == pygame.K_b) or (event.key == pygame.K_c) or (event.key == pygame.K_d) or (event.key == pygame.K_e) or (event.key == pygame.K_f) or (event.key == pygame.K_g) or (event.key == pygame.K_h) or (event.key == pygame.K_i) or (event.key == pygame.K_j) or (event.key == pygame.K_k) or (event.key == pygame.K_l) or (event.key == pygame.K_m) or (event.key == pygame.K_n) or (event.key == pygame.K_o) or (event.key == pygame.K_p) or (event.key == pygame.K_q) or (event.key == pygame.K_r) or (event.key == pygame.K_s) or (event.key == pygame.K_t) or (event.key == pygame.K_u) or (event.key == pygame.K_v) or (event.key == pygame.K_w) or (event.key == pygame.K_x) or (event.key == pygame.K_y) or (event.key == pygame.K_z):
                            usernameInput += event.unicode
                            usernameInput = usernameInput.upper()
                            
                        if (event.key == pygame.K_BACKSPACE):
                            usernameInput = usernameInput [0:-1]

                        if (event.key == pygame.K_RETURN):
                            username = usernameInput
                            signInNum = 2

                if (signInNum == 2):
                    if (event.type == pygame.KEYDOWN):
                        if (event.key == pygame.K_a) or (event.key == pygame.K_b) or (event.key == pygame.K_c) or (event.key == pygame.K_d) or (event.key == pygame.K_e) or (event.key == pygame.K_f) or (event.key == pygame.K_g) or (event.key == pygame.K_h) or (event.key == pygame.K_i) or (event.key == pygame.K_j) or (event.key == pygame.K_k) or (event.key == pygame.K_l) or (event.key == pygame.K_m) or (event.key == pygame.K_n) or (event.key == pygame.K_o) or (event.key == pygame.K_p) or (event.key == pygame.K_q) or (event.key == pygame.K_r) or (event.key == pygame.K_s) or (event.key == pygame.K_t) or (event.key == pygame.K_u) or (event.key == pygame.K_v) or (event.key == pygame.K_w) or (event.key == pygame.K_x) or (event.key == pygame.K_y) or (event.key == pygame.K_z):
                            passwordInput += event.unicode
                            passwordInput = passwordInput.upper()
                            
                        if (event.key == pygame.K_BACKSPACE):
                            passwordInput = passwordInput [0:-1]

                        if (event.key == pygame.K_SPACE):
                            password = passwordInput
                            signInNum = 3

                        if (event.key == pygame.K_ESCAPE):
                            signInNum = 1
                            passwordInput = ""
                            password = ""
                            usernameInput = ""
                            username = ""
                            


        #Main menu
        elif (windowDisplay == 3):
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_RETURN):
                    windowDisplay = 4

        #Game
        elif (windowDisplay == 4):
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

    #Splash Screen
    if (windowDisplay == 1):
        window.fill("#000000")
        window.blit(splashScreenText1, splashScreenText1Center)
        window.blit(splashScreenText2, splashScreenText2Center)

    #Signin
    elif (windowDisplay == 2):
        window.fill("#000000")
        window.blit(loginText1, loginText1Center)

        if (signIn == False):
            if (signInNum == 1):
                #Username
                loginText2 = font1.render("Username: " + usernameInput, True, ("#FFFFFF"))
                loginText2Center = loginText2.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(loginText2, loginText2Center)

            elif (signInNum == 2):
                #Username
                loginText2 = font1.render("Username: " + username, True, ("#FFFFFF"))
                loginText2Center = loginText2.get_rect(center = (windowWidth / 2, windowHeight / 2))
                window.blit(loginText2, loginText2Center)

                #Password
                passwordHidden = len(passwordInput)
                passwordHidden = passwordHidden * "*"
                loginText3 = font1.render("Password: " + passwordHidden, True, ("#FFFFFF"))
                loginText3Center = loginText3.get_rect(center = (windowWidth / 2, windowHeight / 1.5))
                window.blit(loginText3, loginText3Center)

            elif (signInNum == 3):
                if ((username != "") and (password != "") and (signInNum == 3)):
                    with open("userInformation.json", "r") as userInformation:
                        userInfo = json.load(userInformation)

                        for x in range(len(userInfo["Users"])):
                            if ((userInfo["Users"][x]["Username"] == username) and (userInfo["Users"][x]["Password"] == password)):
                                userID = userInfo["Users"][x]["UserID"]
                                username = userInfo["Users"][x]["Username"]
                                windowDisplay = 3

        #Signup

    #Main menu
    elif (windowDisplay == 3):
        window.fill("#000000")
        window.blit(mainMenuText1, mainMenuText1Center)

    #Game
    elif (windowDisplay == 4):
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
