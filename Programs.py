import pygame
COLOR = {
    "black": [0, 0, 0],
    "white": [255, 255, 255],
    "red": [255, 0, 100],
    "green": [100, 255, 100],
    "blue": [0, 0, 255]
}


class programs:
    pass

class Window:
    def __init__(self, x, y, width, height, border=None, color=None, screen=None, command=None, text=None):
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

    def check_tap(self, pos_cursor, pos2=None, draw=None):
        if self.x < pos_cursor[0] < (self.x + self.width) and self.y < pos_cursor[1] < self.y + self.height:
            try:
                self.command()
            except TypeError:
                self.command(pos_cursor, pos2, draw)

class Panel:

    window = None
    DRAW = False

    def __init__(self, x, y, width, height, border, color, screen, st_lb):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        self.border = border

        self.color = color
        self.screen = screen

        self.standart_labels = [Window(self.x, self.y, self.width-50, self.height*0.10,  0, COLOR["green"], self.screen, lambda pos_cursor, pos2, move: self.move(pos_cursor, pos2, move)),
                                Window(self.x+(self.width-50), self.y, 50, self.height*0.10, 0, COLOR["red"], self.screen, lambda: self.change(False))
                                ] if st_lb else []

    def otr(self):
        if self.DRAW:
            pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height), self.border)
            for i in self.window:
                i.otr()

    def check_tap(self, pos_cursor, pos2, draw):
        if self.DRAW:
            for i in self.window:
                i.check_tap(pos_cursor, pos2, draw)

    def change(self, per: bool):
        self.DRAW = per

    def __setattr__(self, key, value):
        if key == "window":
            object.__setattr__(self, key, value + self.standart_labels)
        else:
            object.__setattr__(self, key, value)


    def move(self, pos_cursor, pos_2, draw):
        if draw:
            self.x11 = self.x
            self.y11 = self.y

        self.x = pos_cursor[0] + (self.x11 - pos_2[0])
        self.y = pos_cursor[1] + (self.y11 - pos_2[1])

        for num, win in enumerate(self.window):
            if draw:
                exec("self.x{} = win.x".format(num))
                exec("self.y{} = win.y".format(num))

            win.x = pos_cursor[0] + (eval("self.x{}".format(num)) - pos_2[0])
            win.y = pos_cursor[1] + (eval("self.y{}".format(num)) - pos_2[1])

class Calculator(Window, Panel):
    base_x, base_y = [0, 0]

    def __init__(self, x, y, width, height, margin):
        self.base_x, self.base_y = x, y
        self.x, self.y, self.width, self.height, self.margin = self.base_x, self.base_y, width, height, margin

    executor, result_calculate = "", ""

    def create_subwindows(self, screen):
        result, tools, sym = [], [], (" Plus ", " Minus ", " Equal ")
        for i in range(1, 10):
            result.append(Window(x=self.x, y=self.y, width=self.width, height=self.height, border=3, color=COLOR["red"],
                                 screen=screen, command=lambda i=i: print(i), text=f"{i}-blue"))
            if i % 3 == 0:
                tools.append((self.x, self.y))
                self.y, self.x = self.height + self.margin + self.y, self.base_x
            else:
                self.x = self.width + self.margin + self.x

        return result

    @classmethod
    def calculate(cls, choice):
        if choice.isdigit(): cls.executor += choice

        match choice:
            case " Plus ":
                cls.executor += " + "
            case " Minus ":
                cls.executor += " - "
            case " Equal ":
                if len(cls.executor.split(' ')) == 5:
                    exec("a =" + f"{cls.executor}")
                    print(a)
        #print(cls.executor.split(' '))

    def __call__(self, *args, **kwargs):
        return self.create_subwindows(*args)






