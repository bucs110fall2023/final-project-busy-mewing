import pygame

class Shapes:

    def __init__(self):

        """
    __init__ function, no data needs to be initialized
    args: (self) required
    return: (none)
    """
        pass

    def rect_select(self):

        """
    creates the rectangle objects needed for the grid, and returns them in a list
    args: (self) required
    return: (rects_list), a list containing every rectangle object needed for the games on the grid
    """

        self.rect_1 = pygame.Rect(7, 5, 230, 230)
        self.rect_2 = pygame.Rect(249, 5, 230, 230)
        self.rect_3 = pygame.Rect(491, 5, 230, 230)
        self.rect_4 = pygame.Rect(733, 5, 230, 230)
        self.rect_5 = pygame.Rect(7, 245, 230, 230)
        self.rect_6 = pygame.Rect(249, 245, 230, 230)
        self.rect_7 = pygame.Rect(491, 245, 230, 230)
        self.rect_8 = pygame.Rect(733, 245, 230, 230)
        self.rect_9 = pygame.Rect(7, 485, 230, 230)
        self.rect_10 = pygame.Rect(249, 485, 230, 230)
        self.rect_11 = pygame.Rect(491, 485, 230, 230)
        self.rect_12 = pygame.Rect(733, 485, 230, 230)
        self.rect_13 = pygame.Rect(7, 727, 230, 230)
        self.rect_14 = pygame.Rect(249, 727, 230, 230)
        self.rect_15 = pygame.Rect(491, 727, 230, 230)
        self.rect_16 = pygame.Rect(733, 727, 230, 230)

        rects_list = [self.rect_1,
        self.rect_2, 
        self.rect_3, 
        self.rect_4,
        self.rect_5,
        self.rect_6,
        self.rect_7,
        self.rect_8,
        self.rect_9,
        self.rect_10,
        self.rect_11,
        self.rect_12,
        self.rect_13,
        self.rect_14,
        self.rect_15,
        self.rect_16]

        return rects_list
    
    def button_maker(self, screen, color, button_rect):

        """
        draws buttons on the screen using a given pygame rectangle object
        args: (self, screen, color, button_rect) required, pygame display object, string, pygame rectangle object
        return: (none)
        """

        pygame.draw.rect(screen, color, button_rect)
        pygame.draw.rect(screen, "black", button_rect, 4)