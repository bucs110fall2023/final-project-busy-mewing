import pygame 
from src import shapes
from src import simplify
from src import models
import random

class Controller:
  
  def __init__(self):
    
    """
    initializing data for Controller
    args: (self) required
    return: (none) 
    """

    pygame.mixer.init() #initializing pygame.mixer for sounds
    self.screen = pygame.display.set_mode((960, 960)) #setting up the display and initial state loop
    self.state = "MENU"
    self.image = pygame.image.load(r"assets\finalgui.jpg") #loading the image used as the background in every screen
    self.font = pygame.font.Font(None, 72) #initializing a default font variable
    self.rects = shapes.Shapes.rect_select(self) #initializing a list of 16 rectangles which each fill a spot on the grid
    self.hits = 0 # important variables for game loops
    self.taps = 0
    self.rounds = 1
    self.correct_rect = False
    self.guesses = 3
    self.ding = pygame.mixer.Sound(r"assets\ping.mp3") #Sounds for the game
    self.chime = pygame.mixer.Sound(r"assets\chime.mp3")
    self.fail = pygame.mixer.Sound(r"assets\fail.mp3")
  def mainloop(self):
    
    """
    selects the state loop 
    args: (self) required
    return: (none) 
    """
    
    while True: #chooses the desired event loop depending on self.state
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
      if self.state == "SCORES":
        self.scoreloop()

  def menuloop(self):
      
    """
    loop for the menu, to select a game or quit out
    args: (self) required
    return: (none)
    """

    self.hits = 0 #resets essential counting variables for each game when the menu loop begins
    self.rounds = 1
    self.guesses = 3
    self.taps = 0
    self.correct_rect = False

    simplify.Simplify.reset(self) #resets the screen to the standard grid background, this function will be used several times

    models.Models.menu_button_visual(self) #takes care of creating the buttons which will appear in the menu
    
    self.font = pygame.font.Font(None, 72)
    models.Models.menu_text(self) #blits the text for the menu onto the screen

    pygame.display.flip()

    for event in pygame.event.get(): #for loop which detects when a menu button has been clicked and directs the user to the appropriate game, or the high score menu, or quits the program, respective to which button is clicked
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

          if self.button5.collidepoint(event.pos):
            self.state = "SCORES"
            pygame.quit()
            pygame.init()
            self.screen = pygame.display.set_mode((960, 960))
            self.mainloop()

  def scoreloop(self):
    
    """
    loop for the high score menu, you can click 'menu' to return to menu when done
    args: (self) required
    return: (none)
    """

    simplify.Simplify.reset(self)

    self.hs_menu_button = pygame.Rect(25, 750, 180, 180) #creates the rectangle for the button in the high score menu, used to return to the normal menu
    shapes.Shapes.button_maker(self, self.screen, "grey", self.hs_menu_button)
    self.font = pygame.font.Font(None, 72)
    simplify.Simplify.easy_text_blit(self, self.screen, self.font, "Menu", (50, 810), "white") #labels said button with the text 'Menu'

    with open(r'assets\whack-a-mole_score.txt', 'r') as file: #reads the high scores for whack-a-mole and memory test 
      self.whack_score = file.read()
    with open(r'assets\memory-test_score.txt', 'r') as file:
      self.memory_score = file.read()
    
    simplify.Simplify.easy_text_blit(self, self.screen, self.font, "Whack-a-Mole: "+self.whack_score, (280, 320), "white") #displays the two high scores on screen in the high score menu
    simplify.Simplify.easy_text_blit(self, self.screen, self.font, "Memory Test: "+self.memory_score, (300, 400), "white")

    pygame.display.flip()

    for event in pygame.event.get(): #for loop which will return the user to the standard menu when clicking the button labeled 'Menu' in the high score menu
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if self.hs_menu_button.collidepoint(event.pos):
            self.state = "MENU"
            pygame.quit()
            pygame.init()
            self.screen = pygame.display.set_mode((960, 960))
            self.mainloop()

  def moleloop(self):

    """
    loop to run the whack-a-mole game
    args: (self) required
    return: (none)
    """
    
    simplify.Simplify.reset(self)

    self.font = pygame.font.Font(None, 72)
    simplify.Simplify.easy_text_blit(self, self.screen, self.font, str(self.hits), (465, 10), "grey") #displays your current score as the whack-a-mole game progresses
    
    self.random_rect = random.choice(self.rects) #chooses a random rectangle from the list of 16 which each represent a tile of the grid

    pygame.draw.rect(self.screen, "white", self.random_rect) #draws the randomly chosen rectangle in white
    pygame.display.flip()
    pygame.time.wait(1000)

    for event in pygame.event.get(): #for loop which detects if the user clicks the correct square within 1 second; continues the game if successful, but if clicking an incorrect square, starts the game over loop for whack-a-mole
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          if self.random_rect.collidepoint(event.pos):
            self.hits += 1
            self.ding.play() #plays a sound to indicate a successful hit
            self.mainloop()
          else:
            self.state = "MOLE_END"
            self.mainloop()

    self.state = "MOLE_END" #ends the whack-a-mole game if the user does not click in time
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

    simplify.Simplify.easy_text_blit(self, self.screen, self.font, "Your score was: "+str(self.hits), (280, 10), "grey") #displays the final score achieved after ending whack-a-mole

    pygame.display.flip()
    pygame.time.wait(3000)

    with open(r'assets\whack-a-mole_score.txt', 'r') as file: #rewrites the user's high score on the whack-a-mole game into a text file if the score achieved this time is higher than the high score in the text file
      self.whack_score = file.read()
    if int(self.whack_score) < self.hits:
      with open(r'assets\whack-a-mole_score.txt', 'w') as file:
        file.write(str(self.hits))

    self.state = "MENU" #returns to menu
    self.mainloop()


  def memoryloop(self):

    """
    loop which handles the memory test game
    args: (self) required
    return: (none)
    """

    self.chime.play() #plays a sound to begin each round
    self.taps = 0 #resets the number of clicked white squares each round
    self.good_rects = [] #list which will be used to select random, 'good' white squares that the user must click each round

    simplify.Simplify.reset(self)

    self.font = pygame.font.Font(None, 72)
    simplify.Simplify.easy_text_blit(self, self.screen, self.font, "Round "+str(self.rounds), (380, 10), "grey") #displays the current round each loop

    pygame.display.flip()
    pygame.time.wait(1000)
    simplify.Simplify.reset(self)
    pygame.display.flip()

    for i in self.rects: #fills the screen with black squares
      pygame.draw.rect(self.screen, "black", i)

    for i in range(8): #randomly chooses rectangles to be displayed white and determined as 'good' (needing to be clicked) each round
      self.rand_rect = random.choice(self.rects)
      self.good_rects.append(self.rand_rect)
    
    for i in self.good_rects: #draws the 'good' squares
      pygame.draw.rect(self.screen, "white", i)

    self.needed_taps = len(self.good_rects) #determines the amount of squares which need to be clicked by the user based on how many 'good' squares are chosen for the round

    pygame.display.flip()
    pygame.time.wait(1500)

    for i in self.good_rects: #covers up the screen with all black squares after the white squares are shown so that the user must memorize which ones were white, and click them
      pygame.draw.rect(self.screen, "black", i)
    
    pygame.display.flip()
    pygame.time.wait(3000)

    for event in pygame.event.get(): #for loop which adds to the 'tap' count when a 'good' square is clicked within the time limit
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
    
    if self.taps >= self.needed_taps: #if the user clicked all of the 'good' squares in time, the game goes to the next round; if not, the game over loop for memory test begins
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

    if self.rounds != 1: #fixes the plural text for if the user only lasts one round
      self.text = self.font.render("You lasted for "+str(self.rounds)+" rounds", True, "grey")
    elif self.rounds == 1:
      self.text = self.font.render("You lasted for "+str(self.rounds)+" round", True, "grey")

    self.screen.blit(self.text, (220, 10)) #displays the amount of rounds the user survived on screen

    with open(r'assets\memory-test_score.txt', 'r') as file: #checks the current high score for memory test and overwrites it if the user's score was higher this time
      self.memory_score = file.read()
    if int(self.memory_score) < self.rounds:
      with open(r'assets\memory-test_score.txt', 'w') as file:
        file.write(str(self.rounds))

    pygame.display.flip()
    pygame.time.wait(3000)

    self.state = "MENU" #returns to menu
    self.mainloop()

  def guessloop(self):
    
    """
    loop for handling the guess the square game
    args: (self) required
    return: (none)
    """

    if self.correct_rect is False: #if the correct rectangle has not been guessed, then with three guesses left, a random square is chosen to be correct, with 1 or 2, it remains as it was previously, with 0 (or if a negative value is somehow achieved), the user is taken to the game over loop for guess the square
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

      models.Models.guess_draw(self) #displays the number of guesses remaining, and fills the screen with black squares so that the user can make a guess

      for event in pygame.event.get(): #if the user clicks the correct square, they win the game, and self.correct is set to True so that when the loop restarts, the user is shown the good square and told that they have won; if they guess incorrectly, a guess is subracted and the loop will begin again
        if event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if self.good_rect.collidepoint(event.pos):
              self.correct_rect = True
            else:
              self.guesses -= 1
              self.mainloop()

    elif self.correct_rect is True: #if the user chose the correct square, this sequence occurs
      self.chime.play()
      simplify.Simplify.reset(self) #removes the black squares and plays a good sound for success

      pygame.draw.rect(self.screen, "white", self.good_rect) #shows the correct square on screen
      self.font = pygame.font.Font(None, 72)

      simplify.Simplify.easy_text_blit(self, self.screen, self.font, "You chose the correct square!", (160, 10), "grey") #shows the user on screen that they have won

      pygame.display.flip()
      pygame.time.wait(3000)
      self.state = "MENU" #returns to menu
      self.mainloop()

  def guess_end(self): #happens at 0 guesses remaining
    
    """
    returns the user to the menu after failing the guess the square game
    args: (self) required
    return: (none)
    """

    self.fail.play() #plays a bad sound and resets the screen
    simplify.Simplify.reset(self)

    pygame.draw.rect(self.screen, "white", self.good_rect) #shows the user which square had been correct

    self.font = pygame.font.Font(None, 72)
    simplify.Simplify.easy_text_blit(self, self.screen, self.font, "You are out of guesses!", (220, 10), "grey") #tells the user they have failed the game

    pygame.display.flip()
    pygame.time.wait(3000)
    self.state = "MENU" #returns to menu
    self.mainloop()