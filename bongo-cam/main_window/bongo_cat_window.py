import tkinter as tk
from config import get_tracked_keys
from keyboard import is_pressed, KeyboardEvent


class Application(tk.Frame):
    tracked_keys: list = []
    keys_pressed: list = []

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
        self.temp = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.label: tk.Label = tk.Label(self.root, textvariable=self.cur_x)
        self.label2: tk.Label = tk.Label(self.root, textvariable=self.cur_y)
        self.label3: tk.Label = tk.Label(self.root, textvariable=self.temp)
        self.label.pack()
        self.label2.pack()
        self.label3.pack()
        self.label.after(0, self.update_mouse_position)
        self.label3.after(0, self.update_pressed_keys)

    def update_mouse_position(self):
        pointer_x, pointer_y = self.root.winfo_pointerxy()
        self.cur_x.set(pointer_x)
        self.cur_y.set(pointer_y)
        self.label.after(32, self.update_mouse_position)

    def update_pressed_keys(self):
        self.keys_pressed.clear()
        for key in self.tracked_keys:
            if is_pressed(key):
                self.keys_pressed.append(key)
        self.temp.set("{}".format(self.keys_pressed))
        self.label3.after(32, self.update_pressed_keys)
