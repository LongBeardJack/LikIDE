import tkinter as tk
from config import config
import importlib
lang = importlib.import_module("lang." + config.lang)


class FileNamePopup:

    root = None
    name = None
    entry = None

    def on_valid(self):
        if self.entry.get() is not "":
            self.name = self.entry.get()
            self.root.quit()
            self.quit()

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x100")
        self.root.title(lang.file_name_popup)

        self.entry = tk.Entry(self.root)
        self.entry.pack()
        tk.Button(self.root, text=lang.valid, command=lambda: self.on_valid()).pack()

    def get_name(self):
        return self.name

    def mainloop(self):
        self.root.mainloop()

    def quit(self):
        self.root.destroy()