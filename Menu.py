from tkinter import *
from veriables import *
from all_usefull_functions import open_and_re_size_image, make_BUTTON_with_image_and_pack_it, make_LABEL_with_image_and_pack_it

"""
Functions activated by buttons.
"""


# Main Functions
def start_game():
    from Snak_the_snake import game_window
    game_window.mainloop()


def close_menu():

    menu_window.destroy()


def start_game_and_close_menu():
    close_menu()
    start_game()


def open_options_menu_frame():
    for part in menu_canvas.winfo_children():
        part.destroy()
    pack_option_menu_frame()


def BACK_open_main_menu_frame():
    for option_item in menu_canvas.winfo_children():
        option_item.destroy()
    pack_main_menu_frame()


# packing functions
def pack_main_menu_frame():
    make_BUTTON_with_image_and_pack_it("start_button", menu_canvas, start_button_image, start_game_and_close_menu, 0.5,
                                       0.15)
    make_BUTTON_with_image_and_pack_it("option_button", menu_canvas, option_button_image, open_options_menu_frame, 0.5,
                                       0.25)
    make_BUTTON_with_image_and_pack_it("exit_button", menu_canvas, exit_button_image, close_menu, 0.5, 0.9)


def pack_option_menu_frame():
    make_BUTTON_with_image_and_pack_it("start_button", menu_canvas, start_button_image, start_game_and_close_menu, 0.5,
                                       0.15)
    pack_options_word_size()
    pack_options_game_speed()
    pack_bad_food_option()
    make_BUTTON_with_image_and_pack_it("back_button", menu_canvas, back_button_image, BACK_open_main_menu_frame, 0.5,
                                       0.9)


def pack_options_word_size():
    make_LABEL_with_image_and_pack_it("world_size", menu_canvas, world_size_image, 0.2, 0.3)
    make_BUTTON_with_image_and_pack_it("small_button", menu_canvas, small_button_image, small_size, 0.2, 0.45)
    make_BUTTON_with_image_and_pack_it("medium_button", menu_canvas, medium_button_image, mid_size, 0.2, 0.55)
    make_BUTTON_with_image_and_pack_it("big_button", menu_canvas, big_button_image, big_size, 0.2, 0.65)


def pack_options_game_speed():
    make_LABEL_with_image_and_pack_it("game_speed", menu_canvas, game_speed_image, 0.5, 0.3)
    make_BUTTON_with_image_and_pack_it("slow_button", menu_canvas, slow_button_image, slow_speed, 0.5, 0.45)
    make_BUTTON_with_image_and_pack_it("normal_button", menu_canvas, normal_button_image, normal_speed, 0.5, 0.55)
    make_BUTTON_with_image_and_pack_it("fast_button", menu_canvas, fast_button_image, fast_speed, 0.5, 0.65)


def pack_bad_food_option():
    make_BUTTON_with_image_and_pack_it("bad_food_button", menu_canvas, bad_food_image, bad_food_on_off, 0.8, 0.45)
    show_on_label_bad_food()
# On label show


def show_on_label_bad_food():
    if BAD_FOOD_ACTIVE:
        menu_canvas.create_image(GAME_WIDTH * 0.8, GAME_HEIGHT * 0.45, image=on_label, tag="bad_food")
    else:
        menu_canvas.delete("bad_food")


"""
Window Set-up
"""


menu_window = Tk()

menu_window.configure(bg=BACKGROUND_COLOR)
menu_window.title("Snak The Snake")
menu_window.resizable(False, False)


# frame for the main menu
menu_canvas = Canvas(bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)


"""
Universal menu images
"""

start_button_image = open_and_re_size_image("start_button", "start_button", 150, 75)
back_button_image = open_and_re_size_image("back_button", "back_button", 100, 100)

"""
start menu images
"""

option_button_image = open_and_re_size_image("options_button", "options_button", 150, 75)
exit_button_image = open_and_re_size_image("exit_button", "exit_button", 90, 45)

"""
options menu images
"""
# Universal images
on_label = open_and_re_size_image("on_label", "on_label", 50, 50)
# World Size
world_size_image = open_and_re_size_image("world_size", "world_size", 90, 90)
small_button_image = open_and_re_size_image("small_button", "small_button", 108, 108)
medium_button_image = open_and_re_size_image("medium_button", "medium_button", 108, 108)
big_button_image = open_and_re_size_image("big_button", "big_button", 108, 108)
# Game Speed
game_speed_image = open_and_re_size_image("game_speed_label", "game_speed", 120, 68)
slow_button_image = open_and_re_size_image("slow_button_speed", "slow_button_speed", 108, 54)
normal_button_image = open_and_re_size_image("normal_button_speed", "normal_button_speed", 108, 54)
fast_button_image = open_and_re_size_image("fast_button_speed", "fast_button_speed", 108, 53)
# Bad Food
bad_food_image = open_and_re_size_image("bad_food_button", "bad_food_button", 75, 75)

"""
Start the Menu and pack the main menu frame
"""

menu_canvas.pack()
pack_main_menu_frame()