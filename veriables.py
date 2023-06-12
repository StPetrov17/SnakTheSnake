"""MAIN Variables needed"""

GAME_WIDTH = 660
GAME_HEIGHT = 660
SPEED = 150
SPACE_SIZE = 30
BODY_PARTS_AT_START = 4
SNAKE_HEAD_COLOR = "#268f06"
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


size_small = 44
size_mid = 30
size_big = 15

speed_slow = 200
speed_mid = 150
speed_fast = 100


"""
Change variables
"""


# size
def small_size():
    global SPACE_SIZE
    SPACE_SIZE = size_small


def mid_size():
    global SPACE_SIZE
    SPACE_SIZE = size_mid


def big_size():
    global SPACE_SIZE
    SPACE_SIZE = size_big


# game speed
def slow_speed():
    global SPEED
    SPEED = speed_slow


def normal_speed():
    global SPEED
    SPEED = speed_mid


def fast_speed():
    global SPEED
    SPEED = speed_fast


"""
BAD FOOD variables needed
"""


BAD_FOOD_ACTIVE = False
FOOD_GOES_BAD = 0
FOOD_WILL_GO_BAD_BASE = 20
FOOD_WILL_GO_BAD = FOOD_WILL_GO_BAD_BASE
TIME_BAD_BASE = 10
TIME_BAD = TIME_BAD_BASE
BAD_FOOD_WILL_DIE = FOOD_WILL_GO_BAD + TIME_BAD
BAD_FOOD_COLOR = "#004d1b"


"""
Bad food change variables
"""


def bad_food_on_off():
    global BAD_FOOD_ACTIVE
    if BAD_FOOD_ACTIVE:
        BAD_FOOD_ACTIVE = False
    else:
        BAD_FOOD_ACTIVE = True