import sys
import tkinter as tk
from main_window import Application
import os

title: str = "Bongo-cam"

running: bool = True


def close_window(app_root: tk.Tk):
    running = False
    for window in app_root.winfo_children():
        window.destroy()
    app_root.destroy()
    exit(0)


def mainloop(app_root: tk.Tk, main_window: Application):
    while running:
        app_root.after(0, main_window.update_mouse_position)
        main_window.update_idletasks()
        main_window.update()


def is_admin() -> bool:
    os_name: str = sys.platform
    if os_name not in ['linux', 'darwin']:
        # Windows does not require administrator access
        return True
    return os.geteuid() == 0


if __name__ == "__main__":
    root = tk.Tk()
    if not is_admin():
        ask_root: tk.Label = tk.Label(root, text="Please, run this program as root")
        exit(-1)
    root.protocol("WM_DELETE_WINDOW", lambda: close_window(root))
    root.title(title)
    bongo_cam = Application(root)
    mainloop(root, bongo_cam)
