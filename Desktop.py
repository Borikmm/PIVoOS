import pygame
import sys
import time
import random
from pygame.color import THECOLORS
import Programs
pygame.init()

class Desktop(Programs.programs):

    dysplay_width, dysplay_hight = pygame.display.Info().current_w, pygame.display.Info().current_h

    color = {
        "black": [0, 0, 0],
        "white": [255, 255, 255],
        "red": [255, 0, 0],
        "green": [0, 255, 0],
        "blue": [0, 0, 255],
        "custom1": [123, 32, 200]
    }
    margin = 180
    FIXED_FRAME = 2
    test = False
    draw = False



    def __init__(self):
        super().__init__()
        pygame.init()

        # start parametres for window
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)#, pygame.FULLSCREEN)

        # background color
        self.screen.fill(THECOLORS['black'])

        self.create_dynamic_panels()


        while True:

            clock = time.time()

            hour = time.localtime(clock).tm_hour if len(str(time.localtime(clock).tm_hour)) == 2 else f"{0}{time.localtime(clock).tm_hour}"
            min = time.localtime(clock).tm_minmin if len(str(time.localtime(clock).tm_min)) == 2 else f"{0}{time.localtime(clock).tm_min}"
            sec = time.localtime(clock).tm_sec if len(str(time.localtime(clock).tm_sec)) == 2 else f"{0}{time.localtime(clock).tm_sec}"
            self.struct = f"{hour}:{min}:{sec}"

            self.create_static_panels()

            pygame.time.Clock().tick(180)

            for i in [self.calculation, self.pan1, self.main_panel]:
                if i.DRAW:
                    i.otr()

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
                        # pan1.check_tap(event.pos, self.pos_cursor, self.test)
                        # calculation2.check_tap(event.pos, self.pos_cursor, self.test)
                        # main_panel.check_tap(event.pos, self.pos_cursor, self.test)

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.draw = False

                if self.draw:
                    self.pan1.check_tap(event.pos, self.pos_cursor, self.test)
                    self.calculation.check_tap(event.pos, self.pos_cursor, self.test)
                    self.main_panel.check_tap(event.pos, self.pos_cursor, self.test)
                    self.test = False


            pygame.display.flip()
            self.screen.fill(self.color["black"])

    def create_dynamic_panels(self):
        self.pan1 = Programs.Panel(200, 100, 200, 500, 0, self.color["white"], self.screen, True)
        win1 = [Programs.Window(300, 400, 100, 100, 2, self.color["blue"], self.screen, lambda: exit(), "exit-red"),
                Programs.Window(300, 200, 100, 100, 2, self.color["red"], self.screen,
                                lambda: print("hello world"))]
        self.pan1.window = win1
        self.pan1.DRAW = False

        self.calculation = Programs.Panel(150, 100, 500, 500, 0, self.color["white"], self.screen, True)
        win2 = Programs.Calculator(200, 250, 60, 60, 20, self.screen)()
        self.calculation.window = win2
        self.calculation.DRAW = False

        self.main_panel = Programs.Panel(x=0, y=self.dysplay_hight - 80, width=self.dysplay_width, height=80, border=0,
                                    color=self.color["white"], screen=self.screen, st_lb=False)

    def create_static_panels(self):
        win_main_panel = [
            Programs.Window(200, self.dysplay_hight - 80, 100, 80, 0, self.color["custom1"], self.screen,
                            lambda: self.pan1.change(True), "деньги-black"),
            Programs.Window(0, self.dysplay_hight - 80, 100, 80, 0, self.color["custom1"], self.screen,
                            lambda: exit(), "exit-black"),
            Programs.Window(500, self.dysplay_hight - 80, 100, 80, 0, self.color["custom1"], self.screen,
                            lambda: self.calculation.change(True), "calc-black"),
            Programs.Text(self.dysplay_width - 150,
                          self.dysplay_hight - 60,
                          self.struct,
                          self.color["custom1"], self.screen)
        ]
        self.main_panel.window = win_main_panel
        self.main_panel.DRAW = True

