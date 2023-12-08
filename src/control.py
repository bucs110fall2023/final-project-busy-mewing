import pygame 
from src import shapes
from src import simplify
import random

class Controller:
  
  def __init__(self):
    
    """
    initializing data for Controller
    args: (self) required
    return: (none) 
    """

    pygame.mixer.init()
    self.screen = pygame.display.set_mode((960, 960))
    self.state = "MENU"
    self.image = pygame.image.load(r"C:\Users\phili\Documents\GitHub\final-project-busy-mewing\assets\finalgui.jpg")
    self.hits = 0
    self.font = pygame.font.Font(None, 72)
    self.rects = shapes.Shapes.rect_select(self)
    self.taps = 0
    self.rounds = 1
    self.correct_rect = False
    self.guesses = 3
    self.ding = pygame.mixer.Sound(r"C:\Users\phili\Documents\GitHub\final-project-busy-mewing\assets\ping.mp3")
    self.chime = pygame.mixer.Sound(r"C:\Users\phili\Documents\GitHub\final-project-busy-mewing\assets\chime.mp3")
    self.fail = pygame.mixer.Sound(r"C:\Users\phili\Documents\GitHub\final-project-busy-mewing\assets\fail.mp3")
  def mainloop(self):
    
    """
    selects the state loop 
    args: (self) required
    return: (none) 
    """
    
    while True:
      if self.state == "MENU":
        self.menuloop()
      if self.state == "MOLE":
        self.moleloop()
      if self.state == "MOLE_END":
        self.mole_end()
      if self.state == "MEMORY":
        self.memoryloop()
      if self.state == "MEMORY_END":
        self.memory_end()
      if self.state == "GUESS":
        self.guessloop()
      if self.state == "GUESS_END":
        self.guess_end()

  def menuloop(self):
      
    """
    loop for the menu, to select a game or quit out
    args: (self) required
    return: (none)
    """

    self.hits = 0
    self.rounds = 1
    self.guesses = 3
    self.taps = 0
    self.correct_rect = False

    simplify.Simplify.reset(self)

    self.button1 = pygame.Rect(280, 120, 400, 240)
    self.button2 = pygame.Rect(280, 410, 400, 240)
    self.button3 = pygame.Rect(280, 700, 400, 240)
    self.button4 = pygame.Rect(25, 750, 180, 180)

    pygame.draw.rect(self.screen, "red", self.button1)
    pygame.draw.rect(self.screen, "black", self.button1, 4)
    pygame.draw.rect(self.screen, "blue", self.button2)
    pygame.draw.rect(self.screen, "black", self.button2, 4)
    pygame.draw.rect(self.screen, "purple", self.button3)
    pygame.draw.rect(self.screen, "black", self.button3, 4)
    pygame.draw.rect(self.screen, "grey", self.button4)
    pygame.draw.rect(self.screen, "black", self.button4, 4)

    self.text = self.font.render("Whack-a-Mole", True, "grey")
    self.screen.blit(self.text, (330, 190))
    self.text = self.font.render("Memory Test", True, "grey")
    self.screen.blit(self.text, (330, 480))
    self.font = pygame.font.Font(None, 64)
    self.text = self.font.render("Guess the Square", True, "grey")
    self.screen.blit(self.text, (290, 770))
    self.text = self.font.render("Welcome to 3-in-1!", True, "grey")
    self.screen.blit(self.text, (280, 15))
    self.text = self.font.render("Choose one of the games below!", True, "grey")
    self.screen.blit(self.text, (160, 55))
    self.text = self.font.render("Quit", True, "white")
    self.screen.blit(self.text, (60, 810))
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if self.button1.collidepoint(event.pos):
            self.state = "MOLE"
            pygame.quit()
            pygame.init()
            self.screen = pygame.display.set_mode((960, 960))
            self.mainloop()

          if self.button2.collidepoint(event.pos):
            self.state = "MEMORY"
            pygame.quit()
            pygame.init()
            self.screen = pygame.display.set_mode((960, 960))
            self.mainloop()

          if self.button3.collidepoint(event.pos):
            self.state = "GUESS"
            pygame.quit()
            pygame.init()
            self.screen = pygame.display.set_mode((960, 960))
            self.mainloop()

          if self.button4.collidepoint(event.pos):
            pygame.quit()

  def moleloop(self) -> None:

    """
    loop to run the whack-a-mole game
    args: (self) required
    return: (none)
    """
    
    simplify.Simplify.reset(self)
    self.font = pygame.font.Font(None, 72)
    self.hits_message = self.font.render(str(self.hits), False, "grey")
    self.screen.blit(self.hits_message, (465, 10))
    
    self.random_rect = random.choice(self.rects)

    pygame.draw.rect(self.screen, "white", self.random_rect)
    pygame.display.flip()
    pygame.time.wait(1000)

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if self.random_rect.collidepoint(event.pos):
            self.hits += 1
            self.ding.play()
            self.mainloop()
          else:
            self.state = "MOLE_END"
            self.mainloop()
    self.state = "MOLE_END"
    self.mainloop()
    
  def mole_end(self):

    """
    returns the user to the menu after failing at whack-a-mole
    args: (self) required
    return: (none)
    """
    self.fail.play()
    simplify.Simplify.reset(self)
    self.font = pygame.font.Font(None, 72)
    self.hits_message = self.font.render("Your score was: "+str(self.hits), False, "grey")
    self.screen.blit(self.hits_message, (280, 10))
    pygame.display.flip()
    pygame.time.wait(3000)
    self.state = "MENU"
    self.mainloop()


  def memoryloop(self):

    """
    loop which handles the memory test game
    args: (self) required
    return: (none)
    """

    self.chime.play()
    self.taps = 0
    self.good_rects = []
    simplify.Simplify.reset(self)
    self.font = pygame.font.Font(None, 72)
    self.text = self.font.render("Round "+str(self.rounds), True, "grey")
    self.screen.blit(self.text, (380, 10))

    pygame.display.flip()
    pygame.time.wait(1000)
    simplify.Simplify.reset(self)
    pygame.display.flip()

    for i in self.rects:
      pygame.draw.rect(self.screen, "black", i)

    for i in range(8):
      self.rand_rect = random.choice(self.rects)
      self.good_rects.append(self.rand_rect)
    
    for i in self.good_rects:
      pygame.draw.rect(self.screen, "white", i)

    self.needed_taps = len(self.good_rects)

    pygame.display.flip()
    pygame.time.wait(2000)

    for i in self.good_rects:
      pygame.draw.rect(self.screen, "black", i)
    
    pygame.display.flip()
    pygame.time.wait(4000)


    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if self.good_rects[0].collidepoint(event.pos):
            self.taps += 1
          if self.good_rects[1].collidepoint(event.pos):
            self.taps += 1
          if self.good_rects[2].collidepoint(event.pos):
            self.taps += 1
          if self.good_rects[3].collidepoint(event.pos):
            self.taps += 1
          if self.good_rects[4].collidepoint(event.pos):
            self.taps += 1
          if self.good_rects[5].collidepoint(event.pos):
            self.taps += 1
          if self.good_rects[6].collidepoint(event.pos):
            self.taps += 1
          if self.good_rects[7].collidepoint(event.pos):
            self.taps += 1
    
    if self.taps >= self.needed_taps:
      self.rounds += 1
      self.mainloop()
    if self.taps < self.needed_taps:
      self.state = "MEMORY_END"
      self.mainloop()

  def memory_end(self):

    """
    returns the user to the menu after failing the memory test game
    args: (self) required
    return: (none)
    """
    self.fail.play()
    simplify.Simplify.reset(self)

    if self.rounds != 1:
      self.text = self.font.render("You lasted for "+str(self.rounds)+" rounds", True, "grey")
    elif self.rounds == 1:
      self.text = self.font.render("You lasted for "+str(self.rounds)+" round", True, "grey")

    self.screen.blit(self.text, (240, 10))

    pygame.display.flip()
    pygame.time.wait(3000)
    self.state = "MENU"
    self.mainloop()

  def guessloop(self):
    
    """
    loop for handling the guess the square game
    args: (self) required
    return: (none)
    """

    if self.correct_rect is False:
      if self.guesses == 3:
        self.good_rect = random.choice(self.rects)
      elif self.guesses > 0 and self.guesses < 3: 
        self.good_rect = self.good_rect
      elif self.guesses == 0:
        self.state = "GUESS_END"
        self.mainloop()
      elif self.guesses < 0:
        self.guesses = 0
        self.state = "GUESS_END"
        self.mainloop()

      self.ding.play()
      simplify.Simplify.reset(self)
      self.font = pygame.font.Font(None, 72)
      if self.guesses != 1:
        self.text = self.font.render("You have "+str(self.guesses)+ " guesses!", True, "grey")
      elif self.guesses == 1:
        self.text = self.font.render("You have "+str(self.guesses)+ " guess!", True, "grey")
      self.screen.blit(self.text, (260, 10))

      pygame.display.flip()
      pygame.time.wait(1000)

      simplify.Simplify.reset(self)
      for i in self.rects:
        pygame.draw.rect(self.screen, "black", i)
      pygame.draw.rect(self.screen, "black", self.good_rect)

      pygame.display.flip()
      pygame.time.wait(4000)

      for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.good_rect.collidepoint(event.pos):
              self.correct_rect = True
            else:
              self.guesses -= 1
              self.mainloop()

    elif self.correct_rect is True:
      self.chime.play()
      simplify.Simplify.reset(self)
      self.font = pygame.font.Font(None, 72)
      pygame.draw.rect(self.screen, "white", self.good_rect)
      self.text = self.font.render("You chose the correct square!", True, "grey")
      self.screen.blit(self.text, (160, 10))

      pygame.display.flip()
      pygame.time.wait(3000)
      self.state = "MENU"
      self.mainloop()

  def guess_end(self):
    
    """
    returns the user to the menu after failing the guess the square game
    args: (self) required
    return: (none)
    """

    self.fail.play()
    self.screen.fill("white")
    self.screen.blit(self.image, (0, 0))
    pygame.draw.rect(self.screen, "white", self.good_rect)
    self.font = pygame.font.Font(None, 72)
    self.text = self.font.render("You are out of guesses!", True, "grey")
    self.screen.blit(self.text, (220, 10))

    pygame.display.flip()
    pygame.time.wait(3000)
    self.state = "MENU"
    self.mainloop()