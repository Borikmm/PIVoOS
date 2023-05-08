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

    pi = 3.141592653

    def __init__(self):

        super().__init__()

        # for debuging
        self.screen = pygame.display.set_mode((800, 800))
        self.screen.fill(THECOLORS['black'])

        clock = pygame.time.Clock()
        self.draw = False

        self.font = pygame.font.Font(None, 25)

        self.objects = {
            "windows": {

            },
            "labels": {
                "pusk-rect": (lambda: pygame.draw.rect(self.screen, self.color["blue"], (20, 750, 30, 40), 2),
                         lambda: self.add_window(pygame.draw.circle, self.screen, self.color["red"], (80, 400), 20),
                         (20, 760)),
                "pusk-circle": (lambda: pygame.draw.circle(self.screen, self.color["blue"], (80, 760), 20),
                         lambda: self.add_window(pygame.draw.circle, self.screen, self.color["red"], (200, 400), 20),
                         (80, 760, 20)),
            }

        }

        while True:
            clock.tick(60)


            for event in pygame.event.get():
                    # pygame.draw.circle(self.screen, self.color["blue"], event.pos, 20)
                    # pygame.draw.rect(self.screen, self.color["red"], [20, 20, event.pos[0], event.pos[1]], 2)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    print("hello world")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.draw = True

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.draw = False

                if self.draw:
                    self.check_tap(event.pos)



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
            self.screen.fill(self.color["black"])

    def window_otr(self):

        for name_label, atr_label in self.objects["windows"].items():
            otr_label = atr_label[0]
            com_label = atr_label[1]
            otr_label()


            if com_label == "move":
                pass

        for name_label, atr_label in self.objects["labels"].items():
            otr_label = atr_label[0]
            com_label = atr_label[1]

            otr_label()

    def check_tap(self, pos_cursor):
        for names_label, atr_label in self.objects["windows"].items():

            type_label, name_label = names_label.split("-")[1], names_label.split("-")[0]

            pos = atr_label[2]
            com_label = atr_label[1]

            match type_label:
                case "circle":
                    rad = pos[2]
                    if pos[0] - rad < pos_cursor[0] < (pos[0] + rad) and pos[1] - rad < pos_cursor[1] < pos[1] + rad:
                        if com_label() == "move":
                            if self.draw:
                                self.objects["windows"][names_label] = self.add_window(pygame.draw.circle, self.screen,
                                                                                      self.color["red"],
                                                                                      (pos_cursor[0], pos_cursor[1]),
                                                                                      20)
                case "rect":
                    pass

        for names_label, atr_label in self.objects["labels"].items():

            type_label, name_label = names_label.split("-")[1], names_label.split("-")[0]

            pos = atr_label[2]
            com_label = atr_label[1]

            match type_label:
                case "circle":
                    rad = pos[2]
                    if pos[0] - rad < pos_cursor[0] < (pos[0] + rad) and pos[1] - rad < pos_cursor[1] < pos[1] + rad:
                        self.objects["windows"][names_label] = com_label()
                case "rect":
                    pass






if __name__ == "__main__":
    Desktop()