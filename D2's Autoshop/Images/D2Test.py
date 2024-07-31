while not finished:
                timer += clock.tick(30)/1000
                backgroundDraw()
                screen.blit(nextButton, (400, 400))
                screen.blit(finalText, (420, 420))
                prompt = promptFont.render("Drive safe!", True, (255, 255, 255))
                screen.blit(prompt, (promptX, promptY))
                if body == body1:
                    wheelX1 += 2
                    wheelX2 += 2
                    bodyX += 2
                elif body == body2:
                    wheelX1 -= 2
                    wheelX2 -= 2
                    bodyX -= 2
                elif body == body3:
                    wheelX1 -= 2
                    wheelX2 -= 2
                    bodyX -= 2
                elif body == body4:
                    wheelX1 -= 2
                    wheelX2 -= 2
                    bodyX -= 2
                screen.blit(body, (bodyX, bodyY))
                screen.blit(wheel, (wheelX1, wheelY))
                screen.blit(wheel, (wheelX2, wheelY))
                print(timer)
                if pygame.mouse.get_pressed()[0] and timer > 10:
                    mousePosition = pygame.mouse.get_pos()
                    if driveButton.get_rect(topleft = (400, 400)).collidepoint(mousePosition):
                        print ("done")
                        finished = True
                        onDriveScreen = False
                        onBodyScreen = True




if event.type == pygame.MOUSEBUTTONDOWN:
                    finished = True
                    print ("hey")
                    mousePosition = pygame.mouse.get_pos()
                    if finalButton.get_rect(topleft = (200, 400)).collidepoint(mousePosition):
                        onDriveScreen = False
                        onBodyScreen = True
                        print ("hi")

