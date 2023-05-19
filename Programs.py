import pygame
from numba import prange
color = {
    "black": [0, 0, 0],
    "white": [255, 255, 255],
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255]
}

class programs:
    pass




class window:
    def __init__(self, x, y, width, height, border, color, screen, command, text=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.border = border

        self.color = color
        self.screen = screen
        self.command = command

        self.text = text

        if self.text:
            self.text = text.split("-")[0]
            self.color_text = text.split("-")[1]

    def otr(self):
        border = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, self.color, border, self.border)
        if self.text:
            font = pygame.font.Font(None, 25)
            text = font.render(self.text, True, self.color_text)
            font_rect = text.get_rect()
            font_rect.center = border.center
            self.screen.blit(text, font_rect)

    def check_tap(self, pos_cursor):
        if self.x < pos_cursor[0] < (self.x + self.width) and self.y < pos_cursor[1] < self.y + self.height:
            self.command()













class Panel:

    window = None
    DRAW = False

    def __init__(self, x, y, width, height, border, color, screen):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.border = border

        self.color = color
        self.screen = screen


    def otr(self):
        if self.DRAW:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border)
            for i in self.window:
                i.otr()

    def check_tap(self, pos_cursor):
        if self.DRAW:
            for i in self.window:
                i.check_tap(pos_cursor)

    def change(self, per: bool):
        self.DRAW = per


class Calculator(window, Panel):
    def __init__(self, x, y, width, height, margin):
        self.x, self.y, self.width, self.height, self.margin = x + margin, y + margin, width, height, margin


    def create_subwindows(self, screen):
        result = []
        for i in prange(1, 10):
            result.append(window(self.x, self.y, self.width, self.height, 3, color["red"], screen, lambda: Panel().change(True), f"{i}-blue"))
            if i in (3,6,9): self.y = self.height + self.margin
            self.x = self.width + self.margin

        return result

    def __call__(self, *args, **kwargs):
        return self.create_subwindows(*args)





    

