#!/usr/bin/env python3

import os
import sys
import tkinter as tk

from main_window import Application

title: str = "Bongo-cam"

running: bool = True


def close_window(app_root: tk.Tk):
    running = False
    for window in app_root.winfo_children():
        window.destroy()
    app_root.destroy()
    exit(0)


def is_admin() -> bool:
    os_name: str = sys.platform
    if os_name not in ['linux', 'darwin']:
        # Windows does not require administrator access
        return True
    return os.geteuid() == 0


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("640x640")
    root.resizable(0, 0)

    if not is_admin():
        ask_root: tk.Label = tk.Label(root, text="Please, run this program as root")
        ask_root.pack()
        root.mainloop()
        exit(42)

    root.protocol("WM_DELETE_WINDOW", lambda: close_window(root))
    root.title(title)

    bongo_cam = Application(root)
    bongo_cam.pack()
    bongo_cam.mainloop()
