import pygame
import sys
import time
import random
from pygame.color import THECOLORS

# for debigung
pygame.init()









class Desktop:
    color = {
        "black": [0, 0, 0],
        "white": [255, 255, 255],
        "red": [255, 0, 0],
        "green": [0, 255, 0],
        "blue": [0, 0, 255]
    }

    pi = 3.141592653

    def __init__(self):

        # for debuging
        self.screen = pygame.display.set_mode((800, 800))
        self.screen.fill(THECOLORS['black'])

        clock = pygame.time.Clock()
        draw = False

        self.font = pygame.font.Font(None, 25)

        self.objects = {
            "windows": {},
            "labels": {
                "pusk": (lambda: pygame.draw.circle(self.screen, self.color["blue"], (20, 790), 20), lambda: None),
            }
        }

        while True:
            clock.tick(30)


            for event in pygame.event.get():

                if draw:
                    pygame.draw.circle(self.screen, self.color["blue"], event.pos, 20)
                    pygame.draw.rect(self.screen, self.color["red"], [20, 20, event.pos[0], event.pos[1]], 2)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print("hello world")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        draw = True

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        draw = False

            #screen.fill(self.color["black"])

            self.window_otr()

            # pygame.draw.line(self.screen, self.color["white"], [0, 0], [100, 100], 5)

            # y_offset = 0
            # while y_offset < 100:
            #     pygame.draw.line(self.screen, self.color["red"], [0, 10 + y_offset], [100, 110 + y_offset], 5)
            #     y_offset += 10
            #
            # text = self.font.render("My text", True, self.color["white"])
            #
            # # Рисуем изображение текста на экран в точке (250, 250)
            # self.screen.blit(text, [250, 250])
            #
            # # Рисуем прямоугольник
            # pygame.draw.rect(self.screen, self.color["red"], [20, 20, 250, 100], 2)
            #
            pygame.display.flip()

    def window_otr(self):
        for a in self.objects["windows"]:
            a()
        for name_label, atr_label in self.objects["labels"].items():
            otr_label = atr_label[0]
            com_label = atr_label[1]

            otr_label()



if __name__ == "__main__":
    Desktop()