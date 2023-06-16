from tkinter import *
from PIL import Image, ImageTk
from veriables import BACKGROUND_COLOR


"""
Item set-up functions
"""


def open_and_re_size_image(image_name: str, file_name: str, x: int, y: int) -> Image:
    button_im = Image.open(f"images/{file_name}.png")
    resized_image = button_im.resize((x, y), Image.LANCZOS)
    image_name = ImageTk.PhotoImage(resized_image)
    return image_name


def make_BUTTON_with_image_and_pack_it(name: str, frame, image: Image, function, relx: float, rely: float)\
        -> None:
    name = Button(frame, image=image, borderwidth=0, bg=BACKGROUND_COLOR, command=function)
    name.place(relx=relx, rely=rely, anchor=CENTER)


def make_LABEL_with_image_and_pack_it(name: str, frame, image: Image, relx: float, rely: float, tag=None) ->\
        None:
    name = Label(frame, image=image, borderwidth=0, bg=BACKGROUND_COLOR, tag=tag)
    name.place(relx=relx, rely=rely, anchor=CENTER)
