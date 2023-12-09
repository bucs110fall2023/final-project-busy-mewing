class Simplify:

    def __init__(self) -> None:
        """
        __init__ function, no data to initialize
        args: (self) required
        returns: (none)
        """
        pass

    def reset(self):
        """
        reduces a commonly used piece of code into one line in the Controller, for reseting the screen to the default background
        args: (self) required
        returns: (none)
        """
        self.screen.fill("white")
        self.screen.blit(self.image, (0, 0))

    def easy_text_blit(self, screen, font, message, coords, color):

        """
        reduces two lines of code into one in the Controller for displaying text on screen
        args: (self, screen, font, message, coords, color) required, pygame display object, pygame font object, string, tuple pair, string
        return: (none)
        """

        self.text = font.render(message, True, color)
        screen.blit(self.text, coords)