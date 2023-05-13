import pygame

class programs:
    @staticmethod
    def add_window(func, screen, color, pos_object, radius):
        value = (
            lambda: func(screen, color, pos_object, radius),
            lambda: "move",
            (pos_object[0], pos_object[1], radius, color) if str(func) == "<built-in function circle>" else (pos_object[0], pos_object[1], pos_object[2], pos_object[3], color)
        )
        return value

    @staticmethod
    def add_panel_pusk(screen, colors, func):
        value = [
            ["rect1", lambda: func(pygame.draw.rect, screen, colors["white"], (200, 200, 20, 20), 2)],
            ["rect2", lambda: func(pygame.draw.rect, screen, colors["white"], (200, 200, 10, 10), 2)],
            ["rect3", lambda: func(pygame.draw.rect, screen, colors["white"], (200, 200, 5, 5), 2)]
        ]
        return value


    

