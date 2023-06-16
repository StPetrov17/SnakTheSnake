from tkinter import *
from veriables import *
from random import *
from all_usefull_functions import make_BUTTON_with_image_and_pack_it, open_and_re_size_image
from PIL import Image, ImageTk


"""
MAIN Classes needed
"""


class Snak:
    """
    The Snake object on the board.
    """
    def __init__(self):
        self.body_size = BODY_PARTS_AT_START
        self.coordinates = []
        self.squares = []

        for i in range(0, self.body_size):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:

            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, outline="#000000",
                                             tag="snake")
            self.squares.append(square)


class Food:
    """
    Creates a food object randomly on the field
    """
    def __init__(self):

        x = randint(0, int((GAME_WIDTH / SPACE_SIZE) - 1)) * SPACE_SIZE
        y = randint(0, int((GAME_HEIGHT / SPACE_SIZE) - 1)) * SPACE_SIZE

        self.coordinates = [x, y]
        # puts the food on the board
        canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag='food', outline="#000000")


"""
BAD FOOD Classes needed
"""
class Bad_food:
    """
    Food becomes bad after X amount of turns
    This class is the same as the Food class, but it excepts 2 variable that should me == to the x and y coordinates
    of the food item that should go bad.
    """
    def __init__(self, x, y):

        xp = x
        yp = y

        self.coordinates = [xp, yp]
        # puts the bad food on the board
        canvas.create_rectangle(xp, yp, xp + SPACE_SIZE, yp + SPACE_SIZE, fill=BAD_FOOD_COLOR, tag='food', outline="#000000")

"""
BAD FOOD functions needed
"""

def food_goes_bad(x, y):
    """
    :param x: coordinate x of the food that will go bad
    :param y: coordinate y of the food that will go bad
    deletes the food item from the canvas and
    :return: bad food object with the x and y of the delete food object
    """
    canvas.delete("food")

    return Bad_food(x, y)


def replace_bad_food():
    """
    sets the timer for bad food activation to 0
    :return: deletes the bad food object and makes a Food one
    """
    global FOOD_GOES_BAD
    if FOOD_GOES_BAD == BAD_FOOD_WILL_DIE:
        FOOD_GOES_BAD = 0
        return delete_and_make_food()


def bad_food_eaten(x_food, y_food, x_snake, y_snake):
    """
    :param x_food: x coordinate of the bad food
    :param y_food: y coordinate of the bad food
    :param x_snake: x coordinate of the snake head
    :param y_snake: x coordinate of the snake head
    :return: True if the snake has eaten the bad food
    """
    if x_food == x_snake and y_food == y_snake:
        return True


"""
MAIN Functions needed
"""


def next_turn(snake: Snak, food: Food):
    """
    :param snake: Snak
    :param food: The food Object
    this is the most importaned function that is responsable for running the game and calling all other needed functions
    """

    # coordinates of the head.
    x, y = snake.coordinates[0]

    # makes adjustments to the head depending on the current position.
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    # the next 3 rows make and place the next part of the snake (in front) (helps with the illusion of movement).
    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR,
                                          outline="#000000",
                                          tag="snake")
    snake.squares.insert(0, square)
    global score, FOOD_GOES_BAD
    # checks if the snake head has touched food, if yes increases the score removes the food and places a new one.
    if x == food.coordinates[0] and y == food.coordinates[1]:
        # if BAD food option is active: this will check if the snake has eaten the bad food and if so stop the game.
        if BAD_FOOD_ACTIVE:
            if FOOD_GOES_BAD < FOOD_WILL_GO_BAD:
                FOOD_GOES_BAD = 0
            else:
                game_over()
                return
        score += 1

        label.config(text=f"Size: {BODY_PARTS_AT_START + score} cm.")

        food = delete_and_make_food()

        # checks if the new food spawned in the snake, if yes, deletes it and spawns a new one.
        while check_food_in_snake(snake, food):
            food = delete_and_make_food()

    # deletes the tale of the snake of no food is eaten (helps with the illusion of movement).
    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]
    # if BAD food option is active: this controls the food being replaces with bad food, and bad food with new food when
    # it express.
    if BAD_FOOD_ACTIVE:
        FOOD_GOES_BAD += 1
        if FOOD_GOES_BAD == FOOD_WILL_GO_BAD:
            food = food_goes_bad(food.coordinates[0], food.coordinates[1])
        elif FOOD_GOES_BAD == BAD_FOOD_WILL_DIE:
            food = replace_bad_food()
            while check_food_in_snake(snake, food):
                food = delete_and_make_food()

    # checks for collisions and ends the game if one is found.
    if check_collisions(snake):
        game_over()
    # repeats this function
    else:
        game_window.after(SPEED, next_turn, snake, food)


"""
Supporting functions
"""


def delete_and_make_food():
    """
    deletes an object with the tag food.
    :return: a food object
    """
    canvas.delete("food")

    return Food()


def change_direction(new_direction):
    """
    checks if the movement of the snake is possible
    """
    global direction

    if new_direction == "left":
        if direction != 'right':
            direction = new_direction

    elif new_direction == "right":
        if direction != 'left':
            direction = new_direction

    elif new_direction == "up":
        if direction != 'down':
            direction = new_direction

    elif new_direction == "down":
        if direction != 'up':
            direction = new_direction


def check_collisions(snake):
    """
    Checks if the object (snake) has hit anything
    """
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    """
    Ends the game!
    """
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("Georgia", 25), text="Game Over",
                       fill="red", tag="game_over")
    # make_BUTTON_with_image_and_pack_it("menu_button", canvas, menu_button_image, open_menu, 0.5, 0.7)
    # make_BUTTON_with_image_and_pack_it("restart_button", canvas, restart_button_image, restart_game, 0.5, 0.8)
    make_BUTTON_with_image_and_pack_it("exit_button", canvas, exit_button_image, close_game, 0.5, 0.9)



def check_food_in_snake(snake, food):
    """
    Checks if the food has spawned in the snake
    """
    x, y = food.coordinates

    for body_part in snake.coordinates:
        if x == body_part[0] and y == body_part[1]:
            return True
    return False


def close_game():
    game_window.destroy()


def open_game():
    game_window.mainloop()


def restart_game():
    for part in canvas.winfo_children():
        part.destroy()
    canvas.delete(ALL)


def open_menu():
    from Menu import menu_window
    close_game()
    if __name__ == "__main__":
        menu_window.mainloop()




"""
Creating of the Window, canvas and label needed for the game
"""


# create the window, give it a name, and dot let it be resized
game_window = Tk()
game_window.title("Snak The Snake")
game_window.resizable(False, False)

# score
score = 0
# starting direction
direction = 'down'

# create a label for the score screen
label = Label(game_window, text=f"Size: {BODY_PARTS_AT_START + score} cm.", font=("Georgia", 25), cursor="star")
label.pack()

# create a canvas for the game
canvas = Canvas(game_window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

game_window.update()

# bind the controls
game_window.bind('<a>', lambda event: change_direction("left"))
game_window.bind('<A>', lambda event: change_direction("left"))
game_window.bind('<d>', lambda event: change_direction("right"))
game_window.bind('<D>', lambda event: change_direction("right"))
game_window.bind('<w>', lambda event: change_direction("up"))
game_window.bind('<W>', lambda event: change_direction("up"))
game_window.bind('<s>', lambda event: change_direction("down"))
game_window.bind('<S>', lambda event: change_direction("down"))

# size the window
window_width = game_window.winfo_width()
window_height = game_window.winfo_height()
screen_width = game_window.winfo_screenwidth()
screen_height = game_window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# spaces cannot be in the ()
game_window.geometry(f"{window_width}x{window_height}+{x}+{y}")


snake = Snak()
food = Food()

next_turn(snake, food)

"""
Images used
"""

restart_button_image = open_and_re_size_image("restart_button", "restart_button", 100, 50)
exit_button_image = open_and_re_size_image("exit_button", "exit_button", 90, 45)
menu_button_image = open_and_re_size_image("menu_button", "menu_button", 100, 50)