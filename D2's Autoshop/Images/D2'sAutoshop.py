import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("D2's Autoshop")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    promptFont = pygame.font.Font("Pacifico.ttf", 40)


    def backgroundDraw():
        background = pygame.image.load('background.png')
        background = pygame.transform.scale(background, (800, 600))
        screen.blit(background, (0, 0))

    backgroundDraw()

    onTitleScreen = True
    onBodyScreen = False
    onCurrentBuildScreen1 = False
    onWheelScreen = False
    onCurrentBuildScreen2 = False
    onEngineScreen = False
    onCurrentBuildScreen3 = False
    onDecalScreen = False
    onFinalBuildScreen = False
    onDriveScreen = False


    startButton = pygame.Surface((100, 50))
    startText = font.render("Start", True, (0, 0, 0))
    driveButton = pygame.Surface((100,50))
    driveText = font.render("Drive", True, (255, 255, 255))
    nextButton = pygame.Surface((100,50))
    nextText = font.render("Next", True, (0, 0, 0))
    prompt = font.render("Build a car!", True, (0, 255, 0))
    promptBorder = pygame.Surface((650,65))

    # Car part variables
    rawBody1 = pygame.image.load('body1.png')
    body1 = pygame.transform.scale(rawBody1, (rawBody1.get_width() * .16, rawBody1.get_height() * .25))
    rawBody2 = pygame.image.load('body2.png')
    body2 = pygame.transform.scale(rawBody2, (rawBody2.get_width() * .40, rawBody2.get_height() * .3))
    rawBody3 = pygame.image.load('body3.png')
    body3 = pygame.transform.scale(rawBody3, (rawBody3.get_width() * .5, rawBody3.get_height() * .5))
    rawBody4 = pygame.image.load('body4.png')
    body4 = pygame.transform.scale(rawBody4, (rawBody4.get_width() * .2, rawBody4.get_height() * .2))
    rawWheel1 = pygame.image.load('wheel1.png')
    wheel1 = pygame.transform.scale(rawWheel1, (rawWheel1.get_width() * .05, rawWheel1.get_height() * .05))
    rawWheel2 = pygame.image.load('wheel2.png')
    wheel2 = pygame.transform.scale(rawWheel2, (rawWheel2.get_width() * .1, rawWheel2.get_height() * .1))
    rawWheel3 = pygame.image.load('wheel3.png')
    wheel3 = pygame.transform.scale(rawWheel3, (rawWheel3.get_width() * .05, rawWheel3.get_height() * .05))
    rawWheel4 = pygame.image.load('wheel4.png')
    wheel4 = pygame.transform.scale(rawWheel4, (rawWheel4.get_width() * .1, rawWheel4.get_height() * .1))
    rawEngine1 = pygame.image.load('engine1.png')
    engine1 = pygame.transform.scale(rawEngine1, (rawEngine1.get_width() * .08, rawEngine1.get_height() * .08))
    rawEngine2 = pygame.image.load('engine2.png')
    engine2 = pygame.transform.scale(rawEngine2, (rawEngine2.get_width() * .25, rawEngine2.get_height() * .25))
    rawEngine3 = pygame.image.load('engine3.png')
    engine3 = pygame.transform.scale(rawEngine3, (rawEngine3.get_width() * .125, rawEngine3.get_height() * .125))
    rawEngine4 = pygame.image.load('engine4.png')
    engine4 = pygame.transform.scale(rawEngine4, (rawEngine4.get_width() * .125, rawEngine4.get_height() * .125))
    rawDecal1 = pygame.image.load('decal1.png')
    decal1 = pygame.transform.scale(rawDecal1, (rawDecal1.get_width() * .1, rawDecal1.get_height() * .1))
    rawDecal2 = pygame.image.load('decal2.png')
    decal2 = pygame.transform.scale(rawDecal2, (rawDecal2.get_width() * .005, rawDecal2.get_height() * .005))
    rawDecal3 = pygame.image.load('decal3.png')
    decal3 = pygame.transform.scale(rawDecal3, (rawDecal3.get_width() * .12, rawDecal3.get_height() * .12))
    rawDecal4 = pygame.image.load('decal4.png')
    decal4 = pygame.transform.scale(rawDecal4, (rawDecal4.get_width() * .03, rawDecal4.get_height() * .03))

    # option coordinates
    option1X = 150
    option1Y = 175
    option1Text = font.render("1", True, (255, 255, 255))
    option2X = 550
    option2Y = 175
    option2Text = font.render("2", True, (255, 255, 255))
    option3X = 150
    option3Y = 400
    option3Text = font.render("3", True, (255, 255, 255))
    option4X = 550
    option4Y = 400
    option4Text = font.render("4", True, (255, 255, 255))

    promptX = 140
    promptY = 15

     # Parts the user selects
    body = ""
    wheel = ""
    engine = ""
    decal = ""

    while True:
        startButton.fill((144,238,144))
        nextButton.fill((255,255,0))
        driveButton.fill((255,127,80))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if onTitleScreen:
            backgroundDraw()
            prompt = promptFont.render("D2's Autoshop", True, (255, 255, 255))
            screen.blit(promptBorder, (130, 25))
            screen.blit(prompt, (promptX, promptY))
            screen.blit(body2, (325, 200))
            screen.blit(wheel2, (345, 260))
            screen.blit(wheel2, (415, 260))
            screen.blit(decal2, (395, 250))
            screen.blit(startButton, (350, 400))
            screen.blit(startText, (370, 420))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                if startButton.get_rect(topleft=(400,400)).collidepoint(mousePosition):
                    onTitleScreen = False
                    onBodyScreen = True

        elif onBodyScreen:
            backgroundDraw()
            prompt = promptFont.render("Choose a car body (press a key)", True, (255, 255, 255))
            screen.blit(promptBorder, (140, 30))
            screen.blit(prompt, (promptX, promptY))
            screen.blit(body1, (option1X, option1Y))
            screen.blit(option1Text, (option1X - 50, option1Y))
            screen.blit(body2, (option2X, option2Y))
            screen.blit(option2Text, (option2X - 50, option2Y))
            screen.blit(body3, (option3X, option3Y))
            screen.blit(option3Text, (option3X - 50, option3Y))
            screen.blit(body4, (option4X, option4Y))
            screen.blit(option4Text, (option4X - 50, option4Y))
            #Does not register a keystroke
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        body = body1
                    elif event.key == pygame.K_2:
                        body = body2
                    elif event.key == pygame.K_3:
                        body = body3
                    elif event.key == pygame.K_4:
                        body = body4
                    onBodyScreen = False
                    onCurrentBuildScreen1 = True


        elif onCurrentBuildScreen1:
            backgroundDraw()
            prompt = promptFont.render("Good start!", True, (255, 255, 255))
            screen.blit(promptBorder, (130, 25))
            screen.blit(prompt, (promptX, promptY))
            screen.blit(body, (300, 150))
            screen.blit(nextButton, (350, 400))
            screen.blit(nextText, (370, 420))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                if nextButton.get_rect(topleft = (350, 400)).collidepoint(mousePosition):
                    onCurrentBuildScreen1 = False
                    onWheelScreen = True

        elif onWheelScreen:
            backgroundDraw()
            prompt = promptFont.render("Choose your wheels", True, (255, 255, 255))
            screen.blit(promptBorder, (130, 25))
            screen.blit(prompt, (promptX, promptY))
            screen.blit(wheel1, (option1X, option1Y))
            screen.blit(option1Text, (option1X - 50, option1Y))
            screen.blit(wheel2, (option2X, option2Y))
            screen.blit(option2Text, (option2X - 50, option2Y))
            screen.blit(wheel3, (option3X, option3Y))
            screen.blit(option3Text, (option3X - 50, option3Y))
            screen.blit(wheel4, (option4X, option4Y))
            screen.blit(option4Text, (option4X - 50, option4Y))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        wheel = wheel1
                    elif event.key == pygame.K_2:
                        wheel = wheel2
                    elif event.key == pygame.K_3:
                        wheel = wheel3
                    elif event.key == pygame.K_4:
                        wheel = wheel4
                    onWheelScreen = False
                    onCurrentBuildScreen2 = True

        elif onCurrentBuildScreen2:
            backgroundDraw()
            prompt = promptFont.render("Badass!", True, (255, 255, 255))
            screen.blit(promptBorder, (130, 25))
            screen.blit(prompt, (promptX, promptY))
            screen.blit(body, (300, 150))
            if body == body1:
                screen.blit(wheel, (310, 245))
                screen.blit(wheel,(400,245))
            elif body == body2:
                screen.blit(wheel, (320, 210))
                screen.blit(wheel, (390,210))
            elif body == body3:
                screen.blit(wheel, (320, 240))
                screen.blit(wheel,(420,240))
            elif body == body4:
                screen.blit(wheel, (320, 190))
                screen.blit(wheel , (420, 190))
            screen.blit(nextButton, (350, 400))
            screen.blit(nextText, (370, 420))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                if nextButton.get_rect(topleft = (350, 400)).collidepoint(mousePosition):
                    onCurrentBuildScreen2 = False
                    onEngineScreen = True


        elif onEngineScreen:
            backgroundDraw()
            prompt = promptFont.render("Choose your engine", True, (255, 255, 255))
            screen.blit(promptBorder, (130, 25))
            screen.blit(prompt, (promptX, promptY))
            screen.blit(engine1, (option1X, option1Y))
            screen.blit(option1Text, (option1X - 50, option1Y))
            screen.blit(engine2, (option2X, option2Y))
            screen.blit(option2Text, (option2X - 50, option2Y))
            screen.blit(engine3, (option3X, option3Y))
            screen.blit(option3Text, (option3X - 50, option3Y))
            screen.blit(engine4, (option4X, option4Y))
            screen.blit(option4Text, (option4X - 50, option4Y))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        engine = engine1
                    elif event.key == pygame.K_2:
                        engine = engine2
                    elif event.key == pygame.K_3:
                        engine = engine3
                    elif event.key == pygame.K_4:
                        engine = engine4
                    onEngineScreen = False
                    onCurrentBuildScreen3 = True


        elif onCurrentBuildScreen3:
            backgroundDraw()
            prompt = promptFont.render("Cool whip bro", True, (255, 255, 255))
            screen.blit(promptBorder, (130, 25))
            screen.blit(prompt, (promptX, promptY))
            screen.blit(body, (300, 150))
            if body == body1:
                screen.blit(wheel, (310, 245))
                screen.blit(wheel,(400,245))
            elif body == body2:
                screen.blit(wheel, (320, 210))
                screen.blit(wheel, (390,210))
            elif body == body3:
                screen.blit(wheel, (320, 240))
                screen.blit(wheel,(420,240))
            elif body == body4:
                screen.blit(wheel, (320, 190))
                screen.blit(wheel , (420, 190))
            screen.blit(engine, (100, 175))
            screen.blit(nextButton, (350, 400))
            screen.blit(nextText, (370, 420))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                if nextButton.get_rect(topleft = (350, 400)).collidepoint(mousePosition):
                    onCurrentBuildScreen3 = False
                    onDecalScreen = True

        elif onDecalScreen:
            backgroundDraw()
            prompt = promptFont.render("Choose your decal", True, (255, 255, 255))
            screen.blit(promptBorder, (130, 25))
            screen.blit(prompt, (promptX, promptY))
            screen.blit(decal1, (option1X, option1Y))
            screen.blit(option1Text, (option1X - 50, option1Y))
            screen.blit(decal2, (option2X, option2Y))
            screen.blit(option2Text, (option2X - 50, option2Y))
            screen.blit(decal3, (option3X, option3Y))
            screen.blit(option3Text, (option3X - 50, option3Y))
            screen.blit(decal4, (option4X, option4Y))
            screen.blit(option4Text, (option4X - 50, option4Y))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        decal = decal1
                    elif event.key == pygame.K_2:
                        decal = decal2
                    elif event.key == pygame.K_3:
                        decal = decal3
                    elif event.key == pygame.K_4:
                        decal = decal4
                    onDecalScreen = False
                    onFinalBuildScreen = True

        elif onFinalBuildScreen:
            backgroundDraw()
            prompt = promptFont.render("Your final build:", True, (255, 255, 255))
            screen.blit(promptBorder, (130, 25))
            screen.blit(prompt, (promptX, promptY))
            screen.blit(body, (300, 150))
            if body == body1:
                screen.blit(wheel, (310, 245))
                screen.blit(wheel,(400,245))
            elif body == body2:
                screen.blit(wheel, (320, 210))
                screen.blit(wheel, (390,210))
            elif body == body3:
                screen.blit(wheel, (320, 240))
                screen.blit(wheel,(420,240))
            elif body == body4:
                screen.blit(wheel, (320, 190))
                screen.blit(wheel, (420, 190))

            if body == body1:
                if decal == decal1:
                    screen.blit(decal, (370, 220))
                elif decal == decal2:
                    screen.blit(decal, (350, 230))
                elif decal == decal3:
                    screen.blit(decal, (340, 220))
                elif decal == decal4:
                    screen.blit(decal, (350, 230))
            elif body == body2:
                if decal == decal1:
                    screen.blit(decal, (350, 185))
                elif decal == decal2:
                    screen.blit(decal, (370, 200))
                elif decal == decal3:
                    screen.blit(decal, (360, 185))
                elif decal == decal4:
                    screen.blit(decal, (370, 190))
            elif body == body3:
                if decal == decal1:
                    screen.blit(decal, (370, 225))
                elif decal == decal2:
                    screen.blit(decal, (370, 235))
                elif decal == decal3:
                    screen.blit(decal, (360, 225))
                elif decal == decal4:
                    screen.blit(decal, (380, 230))
            elif body == body4:
                if decal == decal1:
                    screen.blit(decal, (370, 175))
                elif decal == decal2:
                    screen.blit(decal, (370, 185))
                elif decal == decal3:
                    screen.blit(decal, (370, 173))
                elif decal == decal4:
                    screen.blit(decal, (380, 180))
            screen.blit(engine, (100, 175))
            screen.blit(driveButton, (350, 400))
            screen.blit(driveText, (370, 420))
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = pygame.mouse.get_pos()
                if driveButton.get_rect(topleft = (350, 400)).collidepoint(mousePosition):
                    onFinalBuildScreen = False
                    onDriveScreen = True

        elif onDriveScreen:
            timer = 0
            clock.tick (30)/1000
            timer += 1
            screen.blit(body, (300, 150))
            bodyX = 300
            bodyY = 150
            wheelX1 = ""
            wheelX2 = ""
            wheelY = ""
            timer = 0
            finished = False
            if body == body1:
                wheelY = 245
                wheelX1 = 310
                wheelX2 = 400
                if decal == decal1:
                    decalX = 370
                    decalY = 220
                elif decal == decal2:
                    decalX = 350
                    decalY = 230
                elif decal == decal3:
                    decalX = 340
                    decalY = 220
                elif decal == decal4:
                    decalX = 350
                    decalY = 230
            elif body == body2:
                wheelY = 210
                wheelX1 = 320
                wheelX2 = 390
                if decal == decal1:
                    decalX = 350
                    decalY = 185
                elif decal == decal2:
                    decalX = 370
                    decalY = 200
                elif decal == decal3:
                    decalX = 360
                    decalY = 185
                elif decal == decal4:
                    decalX = 370
                    decalY = 190
            elif body == body3:
                wheelY = 240
                wheelX1 = 320
                wheelX2 = 420
                if decal == decal1:
                    decalX = 370
                    decalY = 225
                elif decal == decal2:
                    decalX = 370
                    decalY = 235
                elif decal == decal3:
                    decalX = 360
                    decalY = 225
                elif decal == decal4:
                    decalX = 380
                    decalY = 230
            elif body == body4:
                wheelY = 190
                wheelX1 = 320
                wheelX2 = 420
                if decal == decal1:
                    decalX = 370
                    decalY = 175
                elif decal == decal2:
                    decalX = 370
                    decalY = 185
                elif decal == decal3:
                    decalX = 370
                    decalY = 173
                elif decal == decal4:
                    decalX = 380
                    decalY = 180
            while onDriveScreen:
                clock.tick(30)/100000
                timer += 1
                backgroundDraw()
                prompt = promptFont.render("Drive safely!", True, (255, 255, 255))
                screen.blit(promptBorder, (130, 25))
                screen.blit(prompt, (promptX, promptY))
                if body == body1:
                    wheelX1 += 4
                    wheelX2 += 4
                    bodyX += 4
                    decalX += 4
                elif body == body2:
                    wheelX1 -= 4
                    wheelX2 -= 4
                    bodyX -= 4
                    decalX -= 4
                elif body == body3:
                    wheelX1 -= 4
                    wheelX2 -= 4
                    bodyX -= 4
                    decalX -= 4
                elif body == body4:
                    wheelX1 -= 4
                    wheelX2 -= 4
                    bodyX -= 4
                    decalX -= 4
                #even when it sets restarts to title screen, these images are still visible (they are in the while loop)
                screen.blit(body, (bodyX, bodyY))
                screen.blit(wheel, (wheelX1, wheelY))
                screen.blit(wheel, (wheelX2, wheelY))
                screen.blit(decal, (decalX, decalY))
                print(timer)
                if timer == 70:
                    onDriveScreen = False
                    onTitleScreen = True


                pygame.display.update()


        pygame.display.update()

if __name__ == '__main__':
    main()
