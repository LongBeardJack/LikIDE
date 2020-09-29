import tkinter as tk


class Window:

    EDITOR = 0
    EXPLORER = 1
    CONSOLE = 2

    root = None
    panes = []
    labels = []
    buttons = []

    def __init__(self, title="Title", geometry="300x300", color="#101010"):
        self.root = tk.Tk()

        self.root.geometry(geometry)
        self.root.title(title)

        editor_pane = tk.PanedWindow(bd=1, bg=color, orient=tk.VERTICAL)
        editor_pane.pack()
        self.panes.append(editor_pane)

        explorer_pane = tk.PanedWindow(bd=2, bg=color, orient=tk.VERTICAL)
        explorer_pane.pack()
        self.panes.append(explorer_pane)

    def mainloop(self):
        self.root.mainloop()

    def create_label(self, **kwargs):
        self.labels.append(tk.Label(self.root, kwargs))

    def add_label(self, index, **kwargs):
        self.labels[index].pack(kwargs)

    def add_all_labels(self, **kwargs):
        for label in self.labels:
            label.pack(kwargs)

    def create_button(self, pane_index, **kwargs):
        self.buttons.append(tk.Button(self.panes[pane_index], kwargs))

    def add_button(self, pane_index, index):
        self.panes[pane_index].add(self.buttons[index])

    def add_all_buttons(self, **kwargs):
        for button in self.buttons:
            button.pack(kwargs)


#class Frame(tk.Frame):

    #def __init__(self):