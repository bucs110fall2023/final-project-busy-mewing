from src import shapes
from src import simplify
import pygame

class Models:

    def __init__(self):
        """
        initialization function, no data to initialize
        args: (self) required
        return: (none)
        """

        pass

    def menu_text(self):
        
        """
        function which blits the standard menu text onto the screen when called
        args: (self) required
        return: (none)
        """

        simplify.Simplify.easy_text_blit(self, self.screen, self.font, "Whack-a-Mole", (310, 190), "white") #each of these texts will be mapped onto a visual button as a label
        simplify.Simplify.easy_text_blit(self, self.screen, self.font, "Memory Test", (330, 480), "white")
        self.font = pygame.font.Font(None, 64)
        simplify.Simplify.easy_text_blit(self, self.screen, self.font, "Guess the Square", (290, 770), "white")
        simplify.Simplify.easy_text_blit(self, self.screen, self.font, "Welcome to 3-in-1!", (280, 15), "white")
        simplify.Simplify.easy_text_blit(self, self.screen, self.font, "Choose one of the games below!", (160, 55), "white")
        simplify.Simplify.easy_text_blit(self, self.screen, self.font, "Quit", (60, 810), "white")
        simplify.Simplify.easy_text_blit(self, self.screen, self.font, "High", (60, 510), "white")
        simplify.Simplify.easy_text_blit(self, self.screen, self.font, "Scores", (45, 550), "white")

    def menu_button_visual(self):

        """
        function which blits the standard menu buttons onto the screen when called
        args: (self) required
        return: (none)
        """

        self.button1 = pygame.Rect(280, 120, 400, 240) #defining the rectangle dimensions for each menu button
        self.button2 = pygame.Rect(280, 410, 400, 240)
        self.button3 = pygame.Rect(280, 700, 400, 240)
        self.button4 = pygame.Rect(25, 750, 180, 180)
        self.button5 = pygame.Rect(25, 440, 180, 250)

        shapes.Shapes.button_maker(self, self.screen, "red", self.button1) #calls a function which draws a filled in rectangle with a chosen color, and a second for a black outline, for each menu button
        shapes.Shapes.button_maker(self, self.screen, "blue", self.button2)
        shapes.Shapes.button_maker(self, self.screen, "purple", self.button3)
        shapes.Shapes.button_maker(self, self.screen, "grey", self.button4)
        shapes.Shapes.button_maker(self, self.screen, "orange", self.button5)

    def guess_draw(self):

        """
        handles most of the drawing of rectangles onto the screen for the guessing game
        args: (self) required
        return: (none)
        """

        self.ding.play() #plays a ding and resets the screen each time the guessloop occurs until either a victory or loss
        simplify.Simplify.reset(self)

        self.font = pygame.font.Font(None, 72) #displays on the screen how many guesses remain (1 or 2 or 3)
        if self.guesses != 1:
            self.text = self.font.render("You have "+str(self.guesses)+ " guesses!", True, "grey")
        elif self.guesses == 1:
            self.text = self.font.render("You have "+str(self.guesses)+ " guess!", True, "grey")
        self.screen.blit(self.text, (260, 10))

        pygame.display.flip()
        pygame.time.wait(1000)
        simplify.Simplify.reset(self)

        for i in self.rects: #fills the screen with black squares for the user to make a guess
            pygame.draw.rect(self.screen, "black", i)
        pygame.draw.rect(self.screen, "black", self.good_rect)

        pygame.display.flip() #the user has 4 seconds to make their guess
        pygame.time.wait(4000)