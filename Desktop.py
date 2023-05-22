import pygame
import sys
import time
import random
from pygame.color import THECOLORS
import Programs

# for debigung
pygame.init()

class Desktop(Programs.programs):

    dysplay_width, dysplay_hight = pygame.display.Info().current_w, pygame.display.Info().current_h
    print(dysplay_hight)

    color = {
        "black": [0, 0, 0],
        "white": [255, 255, 255],
        "red": [255, 0, 0],
        "green": [0, 255, 0],
        "blue": [0, 0, 255]
    }
    margin = 180
    FIXED_FRAME = 2
    test = False
    draw = False



    def __init__(self):
        super().__init__()

        # start parametres for window
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)#, pygame.FULLSCREEN)

        # background color
        self.screen.fill(THECOLORS['black'])



        pan1 = Programs.Panel(200, 100, 200, 500, 0, self.color["white"], self.screen, True)
        win1 = [Programs.Window(300, 400, 100, 100, 2, self.color["blue"], self.screen, lambda: exit(), "exit-red"),
                Programs.Window(300, 200, 100, 100, 2, self.color["red"], self.screen, lambda: print("hello world"))]
        pan1.window = win1
        pan1.DRAW = False

        calculation = Programs.Panel(150, 100, 500, 500, 0, self.color["green"], self.screen, True)
        win2 = Programs.Calculator(150, 100, 50, 50, 50).create_subwindows(self.screen)
        calculation.window = win2
        calculation.DRAW = False


        main_panel = Programs.Panel(x=0, y=self.dysplay_hight-80, width=self.dysplay_width, height=80, border=0, color=self.color["green"], screen=self.screen, st_lb=False)
        win_main_panel = [
            Programs.Window(200, self.dysplay_hight-80, 100, 80, 0, self.color["red"], self.screen, lambda: pan1.change(True), "деньги-blue"),
            Programs.Window(0, self.dysplay_hight-80, 100, 80, 0, self.color["red"], self.screen, lambda: exit(), "exit-blue"),
            Programs.Window(500, self.dysplay_hight-80, 100, 80, 0, self.color["red"], self.screen, lambda: calculation.change(True), "calc-blue"),

        ]
        main_panel.window = win_main_panel
        main_panel.DRAW = True


        while True:
            pygame.time.Clock().tick(180)

            calculation.otr()
            pan1.otr()
            main_panel.otr()


            for event in pygame.event.get():
                    # pygame.draw.circle(self.screen, self.color["blue"], event.pos, 20)
                    # pygame.draw.rect(self.screen, self.color["red"], [20, 20, event.pos[0], event.pos[1]], 2)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print("hello world")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.pos_cursor = event.pos
                    if event.button == 1:
                        self.draw = True
                        self.test = True
                        # pan1.check_tap(event.pos)
                        # calculation.check_tap(event.pos)
                        # main_panel.check_tap(event.pos)

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.draw = False




                if self.draw:
                    pan1.check_tap(event.pos, self.pos_cursor, self.test)
                    calculation.check_tap(event.pos, self.pos_cursor, self.test)
                    main_panel.check_tap(event.pos, self.pos_cursor, self.test)
                    self.test = False




            pygame.display.flip()
            self.screen.fill(self.color["black"])
