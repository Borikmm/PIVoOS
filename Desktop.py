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

        Programs.programs.__init__(self)

        # for debuging
        self.screen = pygame.display.set_mode((800, 800))
        self.screen.fill(THECOLORS['black'])

        clock = pygame.time.Clock()
        self.draw = False

        self.font = pygame.font.Font(None, 25)

        win1 = [Programs.window(100, 100, 200, 300, 2, self.color["red"], self.screen, lambda: print("hello world")),
                Programs.window(100, 100, 300, 400, 2, self.color["blue"], self.screen, lambda: print("hello world")),
                Programs.window(100, 100, 100, 200, 2, self.color["red"], self.screen, lambda: print("hello world"))]


        while True:
            clock.tick(180)

            for i in win1:
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

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.draw = False

                if self.draw:
                    for i in win1:
                        i.check_tap(event.pos)

            pygame.display.flip()
            self.screen.fill(self.color["black"])
