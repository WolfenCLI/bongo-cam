import tkinter as tk

import PIL

from config import get_tracked_keys
from keyboard import is_pressed
from PIL import ImageTk


def keyboard_column(pressed_keys: list) -> int:
    first_column: list = ['Q', 'W', 'E', 'A', 'S', 'D', 'Z', 'X', 'C']
    second_column: list = ['R', 'T', 'Y', 'F', 'G', 'H', 'V', 'B']
    if pressed_keys[0] in first_column:
        return 1  # starting from 1 feels weird lol
    elif pressed_keys[0] in second_column:
        return 2
    else:
        return 3


class Application(tk.Frame):
    tracked_keys: list = []
    keys_pressed: list = []
    images: dict = {}

    def __init__(self, root: tk.Tk):
        super().__init__(root)
        self.root: tk.Tk = root
        self.cur_x: tk.IntVar = tk.IntVar()
        self.cur_y: tk.IntVar = tk.IntVar()
        self.initialize_images()
        self.current_image = ImageTk.PhotoImage(self.images['background'])
        self.canvas: tk.Canvas = tk.Canvas(self, bg="green", width=self.images['background'].width,
                                           height=self.images['background'].height)  # Image is 640 x 640

        self.tracked_keys = get_tracked_keys()
        self.pack()
        self.create_widgets()
        self.after(0, self.update_pressed_keys)
        self.after(0, self.update_mouse_position)
        self.after(0, self.update_canvas)

    def create_widgets(self):
        self.canvas.pack()
        self.canvas.create_image((self.current_image.width() / 2, self.current_image.height() / 2),
                                 image=self.current_image)

    def update_mouse_position(self):
        pointer_x, pointer_y = self.root.winfo_pointerxy()
        self.cur_x.set(pointer_x)
        self.cur_y.set(pointer_y)
        self.after(32, self.update_mouse_position)

    def update_pressed_keys(self):
        self.keys_pressed.clear()
        for key in self.tracked_keys:
            if is_pressed(key):
                self.keys_pressed.append(key)
        self.after(32, self.update_pressed_keys)

    def update_canvas(self):
        tmp_image = self.images['background']
        if len(self.keys_pressed) == 0:
            # No keys pressed. Use defaultLPaw.png
            tmp_image = PIL.Image.alpha_composite(tmp_image, self.images['defaultLPaw'])
        else:
            column: int = keyboard_column(self.keys_pressed)
            if column == 1:
                tmp_image = PIL.Image.alpha_composite(tmp_image, self.images['column1'])
            elif column == 2:
                tmp_image = PIL.Image.alpha_composite(tmp_image, self.images['column2'])
            else:
                tmp_image = PIL.Image.alpha_composite(tmp_image, self.images['column3'])

        # Mouse
        # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.transform

        self.current_image = ImageTk.PhotoImage(tmp_image)

        self.canvas.delete("all")
        self.canvas.create_image((self.current_image.width() / 2, self.current_image.height() / 2),
                                 image=self.current_image)

        self.canvas.after(32, self.update_canvas)

    def initialize_images(self):
        self.images['background'] = PIL.Image.open("./images/background.png").convert("RGBA")
        self.images['defaultLPaw'] = PIL.Image.open("./images/defaultLPaw.png").convert("RGBA")
        self.images['column1'] = PIL.Image.open("./images/QWE.png").convert("RGBA")
        self.images['column2'] = PIL.Image.open("./images/RTY.png").convert("RGBA")
        self.images['column3'] = PIL.Image.open("./images/UIOP.png").convert("RGBA")
