import tkinter as tk


class Window:

    root = None
    labels = []

    def __init__(self, title="Title", geometry="300x300"):
        self.root = tk.Tk()

        self.root.geometry(geometry)
        self.root.title(title)

    def mainloop(self):
        self.root.mainloop()

    def create_label(self, **kwargs):
        self.labels.append(tk.Label(self.root, kwargs))

    def add_label(self, index, **kwargs):
        self.labels[index].pack(kwargs)

    def add_all_label(self, **kwargs):
        for label in self.labels:
            label.pack(kwargs)