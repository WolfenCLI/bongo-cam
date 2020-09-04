import tkinter as tk
from config import get_tracked_keys
from keyboard import is_pressed


class Application(tk.Frame):
    keys_pressed: list = []
    tracked_keys: list = []

    def __init__(self, root: tk.Tk):
        super().__init__(root)
        self.root: tk.Tk = root
        self.cur_x: tk.IntVar = tk.IntVar()
        self.cur_y: tk.IntVar = tk.IntVar()
        pointer_x, pointer_y = self.root.winfo_pointerxy()
        self.cur_x.set(self.root.winfo_rootx() - pointer_x)
        self.cur_y.set(self.root.winfo_rooty() - pointer_y)
        self.tracked_keys = get_tracked_keys()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        label: tk.Label = tk.Label(self.root, textvariable=self.cur_x)
        label2: tk.Label = tk.Label(self.root, textvariable=self.cur_y)
        label.pack()
        label2.pack()

    def update_mouse_position(self):
        pointer_x, pointer_y = self.root.winfo_pointerxy()
        self.cur_x.set(pointer_x)
        self.cur_y.set(pointer_y)

    def update_pressed_keys(self):
        self.keys_pressed.clear()
        for key in self.tracked_keys:
            if is_pressed(key):
                self.keys_pressed.append(key)
