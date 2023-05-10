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
    def add_panel_pusk(screen, colors):
        pos_object = None
        value1 = (
            [lambda: pygame.draw.rect(screen, colors["green"], pos_object, radius), lambda: func(screen, color, pos_object, radius)],
            lambda: "panel",
            (pos_object[0], pos_object[1], radius, color) if str(func) == "<built-in function circle>" else (pos_object[0], pos_object[1], pos_object[2], pos_object[3], color)
        )
        return value


    

