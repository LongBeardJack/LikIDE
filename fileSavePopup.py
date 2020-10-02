import tkinter as tk
from config import config
import importlib

lang = importlib.import_module("lang." + config.lang)


class FileSavePopup:
    root = None
    choice = 0

    def on_valid(self, index):
        self.choice = index
        self.root.quit()

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x100")
        self.root.title(lang.file_save_popup)

        tk.Label(self.root, text=lang.file_save_dialog).pack()

        tk.Button(self.root, text=lang.save, command=lambda: self.on_valid(0)).pack()
        tk.Button(self.root, text=lang.no_save, command=lambda: self.on_valid(1)).pack()
        tk.Button(self.root, text=lang.cancel, command=lambda: self.on_valid(2)).pack()

    def get_choice(self):
        return self.choice

    def mainloop(self):
        self.root.mainloop()

    def quit(self):
        try:
            self.root.destroy()
        finally:
            pass
