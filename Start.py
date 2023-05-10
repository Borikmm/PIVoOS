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
    FIXED_FRAME = 2
    test = False

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
                "panel-rect": (lambda: pygame.draw.rect(self.screen, self.color["blue"], (20, 750, 30, 40), 2),
                         lambda: self.add_window(pygame.draw.rect, self.screen, self.color["red"], (50, 400, 40, 40), 2),
                         (20, 750, 30, 40, self.color["red"])),
                "panel1-rect": (lambda: pygame.draw.rect(self.screen, self.color["green"], (20, 700, 30, 40), 2),
                               lambda: self.add_panel_pusk(self.screen, self.color, (100, 600, 40, 40), 2),
                               (20, 700, 30, 40, self.color["green"])),
                "pusk-circle": (lambda: pygame.draw.circle(self.screen, self.color["blue"], (80, 760), 20),
                         lambda: self.add_window(pygame.draw.circle, self.screen, self.color["red"], (200, 400), 20),
                         (80, 760, 20, self.color["red"])),
                "pusk1-circle": (lambda: pygame.draw.circle(self.screen, self.color["blue"], (200, 760), 20),
                         lambda: self.add_window(pygame.draw.circle, self.screen, self.color["blue"], (300, 400), 20),
                         (200, 760, 20, self.color["blue"])),
            }

        }

        while True:
            clock.tick(180)


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
                    self.check_tap(event.pos)



            self.window_otr()


            pygame.display.flip()
            self.screen.fill(self.color["black"])

    def window_otr(self):

        for name_label, atr_label in self.objects["windows"].items():
            otr_label = atr_label[0]
            if len(otr_label()) > 4:
                for a in otr_label:
                    a()
            else:
                otr_label()


        for name_label, atr_label in self.objects["labels"].items():
            otr_label = atr_label[0]

            otr_label()

    def check_tap(self, pos_cursor):
        for names_label, atr_label in self.objects["windows"].items():

            type_label, name_label = names_label.split("-")[1], names_label.split("-")[0]

            pos = atr_label[2]
            com_label = atr_label[1]

            match type_label:
                case "circle":
                    rad = pos[2]
                    color = pos[3]
                    if pos[0] - rad < pos_cursor[0] < (pos[0] + rad) and pos[1] - rad < pos_cursor[1] < pos[1] + rad:
                        if com_label() == "move":
                            if self.draw:
                                if self.test:
                                    self.pos_need = (pos[0], pos[1])
                                    self.test = False
                                self.objects["windows"][names_label] = self.add_window(pygame.draw.circle, self.screen,
                                                                                      color,
                                                                                      (pos_cursor[0] + (self.pos_need[0] - self.pos_cursor[0]) , pos_cursor[1] + (self.pos_need[1] - self.pos_cursor[1])),
                                                                                      rad)
                case "rect":
                    color = pos[4]
                    width = pos[2]
                    height = pos[3]
                    if pos[0] < pos_cursor[0] < (pos[0] + width) and pos[1] < pos_cursor[1] < pos[1] + height:
                        match com_label():
                            case "move":
                                if self.draw:
                                    if self.test:
                                        self.pos_need = (pos[0], pos[1])
                                        self.test = False
                                    self.objects["windows"][names_label] = self.add_window(pygame.draw.rect, self.screen,
                                                                                           color,
                                                                                           (pos_cursor[0] + (self.pos_need[0] - self.pos_cursor[0]), pos_cursor[1] + (self.pos_need[1] - self.pos_cursor[1]), width, height),
                                                                                           self.FIXED_FRAME)
                            case "panel":
                                print("hello_world")

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
                    width = pos[2]
                    height = pos[3]
                    if pos[0] < pos_cursor[0] < (pos[0] + width) and pos[1] < pos_cursor[1] < pos[1] + height:
                        self.objects["windows"][names_label] = com_label()

if __name__ == "__main__":
    Desktop()