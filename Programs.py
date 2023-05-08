

class programs:
    def add_window(self, func, screen, color, pos_object, radius):
        value = (
            lambda: func(screen, color, pos_object, radius),
            lambda: "move",
            (pos_object[0], pos_object[1], radius)
        )
        return value


    

