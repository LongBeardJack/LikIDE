import tkinter as tk
import config
import importlib
lang = importlib.import_module("lang." + config.lang)


class FileSavePopup:

    root = None
    choice = None

    def on_click(self, index):
        self.choice = index
        self.root.destroy()
        print("KO")

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x100")
        self.root.title(lang.file_name_popup)

        tk.Button(self.root, text=lang.save, command=lambda: self.on_click(0)).pack()
        tk.Button(self.root, text=lang.no_save, command=lambda: self.on_click(1)).pack()
        tk.Button(self.root, text=lang.cancel, command=lambda: self.on_click(2)).pack()

    def get_choice(self):
        return self.choice

    def mainloop(self):
        self.root.mainloop()

    def quit(self):
        self.root.quit()