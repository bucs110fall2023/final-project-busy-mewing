from src import control

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
        reduces a commonly used piece of code into one line in the Controller
        args: (self) required
        returns: (none)
        """
        self.screen.fill("white")
        self.screen.blit(self.image, (0, 0))