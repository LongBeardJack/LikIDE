import tkinter as tk


class Window:

    root = None

    def __init__(self, title="Title", geometry="300x300"):
        self.root = tk.Tk()
        self.root.geometry(geometry)
        self.root.title(title)

    def mainloop(self):
        self.root.mainloop()