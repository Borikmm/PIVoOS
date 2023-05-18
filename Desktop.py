import pygame
import sys
import time
import random
from pygame.color import THECOLORS
import Programs

# for debigung
pygame.init()

class Desktop(Programs.programs):
    color = {
        "black": [0, 0, 0],
        "white": [255, 255, 255],
        "red": [255, 0, 0],
        "green": [0, 255, 0],
        "blue": [0, 0, 255]
    }

    FIXED_FRAME = 2
    test = False




    def __init__(self):
        # evev

        Programs.programs.__init__(self)

        # start parametres for window
        self.screen = pygame.display.set_mode((800, 800))#, pygame.FULLSCREEN)

        # background color
        self.screen.fill(THECOLORS['black'])



        pan1 = Programs.Panel(200, 100, 200, 500, 2, self.color["green"], self.screen)
        win1 = [Programs.window(300, 100, 100, 100,  2, self.color["red"], self.screen, lambda: pan1.change(False), "close-red"),
                Programs.window(300, 400, 100, 100, 2, self.color["blue"], self.screen, lambda: exit(), "exit-red"),
                Programs.window(300, 200, 100, 100, 2, self.color["red"], self.screen, lambda: print("hello world"))]
        pan1.window = win1
        pan1.DRAW = False



        main_panel = Programs.Panel(x=0, y=700, width=700, height=100, border=3, color=self.color["green"], screen=self.screen)
        win_main_panel = [
            Programs.window(0, 700, 100, 100, 3, self.color["red"], self.screen, lambda: pan1.change(True), "деньги-blue")
        ]
        main_panel.window = win_main_panel
        main_panel.DRAW = True


        while True:
            pygame.time.Clock().tick(180)

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
                        pan1.check_tap(event.pos)
                        main_panel.check_tap(event.pos)

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.draw_desktop = False



            pygame.display.flip()
            self.screen.fill(self.color["black"])
