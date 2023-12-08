[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803350&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << 3-in-1 >>
## CS110 Final Project  << Fall, 2023 >>

## Team Members

<< Philip N., ??? >>

***

## Project Description

<< A game which has 3 simple games in one package! There is a basic but fast-paced whack-a-mole, a memory game where you must quickly click on all the squares that will become invisible after a short while, and lastly, a guessing game where you get 3 guesses to quickly try and guess which square on the board is the right one!>>

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. << A menu to select your game >>
2. << Whack-a-Mole >>
3. << Memory Test >>
4. << Guess the Square >>
5. << A score or win/loss condition for each game >>

### Classes

- << 1. class Controller: The Controller class is used to update the view, receieve information from the view, feed its methods said information, and update the view using the output from those mthods. This Controller class contains most of the methods that make the game functional. It has the mainloop which selects the loop to start each game or endgame screen, as well as the menu. 
2. class Shapes: This class ultimately only serves one purpose: to create and store shapes necessary for use by the Controller. However, there was only the need for the rectangles which would be throughout each spot in the grid, and so it only has one method, which simply creates and stores in a list each reactangle and returns it.
3. class Simplify: This class is used for functions that can reduce repetitiveness and bloat in the main program. >>

## ATP

<<1. Click the button labeled "Quit" in the menu. Result: exits the program.
2. Alternatively, click the button labeled "Whack-a-Mole" in the menu. Result: begins Whack-a-Mole game.
3. Click the white squares rapidly as they appear. Result: increases your score in the game.
4. Fail to click the white squares in time or click elsewhere on the screen. Result: the game ends and returns you to the menu.
5. Alternatively, click the button labeled "Memory Test" in the menu. Result: begins Memory Test game.
6. Wait for the white squares on screen to turn black along with the rest (or start immediately to make the game easier), then rapidly click every square that had been white. Result: advances to the next round of the game.
7. Fail to click every square that was white in time. Result: the game ends and returns you to the menu.
8. Alternatively, click the button labeled "Guess the Square" in the menu. Result: begins Guess the Square game.
9. Wait until the squares of the grid turn black, and correctly guess which square is 'correct'. Result: you win the game and are returned to the menu.
10. "                                           ", Fail to click a square in time for a guess. Result: the board resets and you do not gain or lose any guesses.
11. "                                           ", and guess an 'incorrect' square. Result: you lose one of three guesses and can guess again.
12. Guess until you reach zero guesses without clicking the correct square. Result: you lose the game and you are returned to the menu.>>
