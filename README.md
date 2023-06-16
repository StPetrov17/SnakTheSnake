# SnakTheSnake
This is a small Game called "Snak The Snake" and it exists because I wanted to start learning the library tkinter.

The main part of this program (The Game) is not mine. I found a build of it online and used it as a skeleton. This is because I had no idea, at the time, how to your this library so I needed a head start, and reading about how it works is... BORING! Seeing and writing it down helps me learn more easily, even if it is not mine. To the original, I have added:

1. A Main Menu with a start, exit, and options button;
2. A Options menu:
3. Custom made Icons and buttons for the menu (except for the Start, Options, and Exit buttons)
4. The ability to change the game's size and speed; (From the button options in the main menu);
5. An option to activate an additional gameplay feature called Bad Food (From the button options in the main menu) (More information about it below 👇);
6. Organisation of the functions and variables for ease of reading;
7. Adding a small explanation to the function and classes for ease of understanding.
BAD FOOD: If active, this makes the food go bad after a set amount of turns. If eaten in this state, it counts as a game over. After a bit more time the rotten food will completely decompose and be replaced by another piece of food on the map. And repeat.

The Game's original code I used comes from https://www.geeksforgeeks.org/snake-game-using-tkinter-python/.

HOW TO PLAY!!!

Game Controls: with the lower and upper case:
- "w" for moving up;
- "s" for moving down;
- "a" for moving left;
- "d" for moving left

Game roles:

 - The game will spawn new food every time you eat the one in play. It cannot appear on the snake!
 - Every piece of food eaten make you one block longer and adds one point to you score (Size: x cm.)

Game over:

- when you hit the wall with the head of the snake;
- when the head of the snake goes in the body of the snake;
- IF the option bad food is active: when you hit food that is rotten.

This was a good learning experience for me. Not sure if I will work on this in the future, but it was Fun!
