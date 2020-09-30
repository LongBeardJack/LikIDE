import tkinter as tk
import config
import importlib
lang = importlib.import_module("lang." + config.lang)


class FileNamePopup:

    root = None
    text = None
    name = None

    def on_valid(self):
        self.name = self.text.get()
        self.root.quit()

    def __init__(self):
        self.root = tk.Tk()
        self.text = tk.StringVar()
        self.root.geometry("300x100")
        self.root.title(lang.file_name_popup)

        tk.Entry(self.root, textvariable=self.text).pack()
        tk.Button(self.root, text=lang.valid, command=lambda: self.on_valid()).pack()

    def get_name(self):
        return self.name

    def mainloop(self):
        self.root.mainloop()