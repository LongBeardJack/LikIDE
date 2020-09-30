import tkinter as tk
from tkinter import font
import config
import importlib

lang = importlib.import_module("lang." + config.lang)


class Window:
    EDITOR = 0
    EXPLORER = 1
    CONSOLE = 2

    bg_color = config.dark_background_color
    fg_color = config.dark_foreground_color

    root = None
    panes = []
    labels = []
    buttons = []
    editor_area = None

    def donothing(self):
        pass

    def change_theme(self):
        print(self.bg_color)
        if self.bg_color == config.light_background_color:
            self.bg_color = config.dark_background_color
            self.fg_color = config.dark_foreground_color
        else:
            self.bg_color = config.light_background_color
            self.fg_color = config.light_foreground_color

    def __init__(self, title="Title", width="300", height="300"):
        self.root = tk.Tk()

        self.root.geometry(str(width) + "x" + str(height))
        self.root.title(title)

        print(font.families())

        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label=lang.new, command=self.donothing)
        file_menu.add_command(label=lang.open, command=self.donothing)
        file_menu.add_command(label=lang.save, command=self.donothing)
        file_menu.add_separator()
        file_menu.add_command(label=lang.exit, command=self.root.quit)
        menu_bar.add_cascade(label=lang.file_menu, menu=file_menu)

        menu_bar.add_command(label=lang.run, command=self.donothing)

        apparence_menu = tk.Menu(menu_bar, tearoff=0)
        apparence_menu.add_command(label=lang.dark_theme, command=self.change_theme)
        apparence_menu.add_command(label=lang.light_theme, command=self.change_theme)
        menu_bar.add_cascade(label=lang.apparence_menu, menu=apparence_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Help Index", command=self.donothing)
        help_menu.add_command(label=lang.about, command=self.donothing)
        menu_bar.add_cascade(label=lang.help_menu, menu=help_menu)

        self.root.config(menu=menu_bar)

        general_pane = tk.PanedWindow(bg=self.bg_color)
        general_pane.pack(fill=tk.BOTH, expand=1)

        editor_pane = tk.PanedWindow(bd=1, orient=tk.HORIZONTAL, width=((self.root.winfo_reqwidth() * 3) * 2))
        editor_pane.option_add('*Font', config.font_family, config.font_size)
        general_pane.add(editor_pane)
        self.panes.append(editor_pane)
        self.editor_area = tk.Text(editor_pane, bg=self.bg_color, fg=self.fg_color)
        editor_pane.add(self.editor_area)

        explorer_pane = tk.PanedWindow(bd=2, orient=tk.VERTICAL, width=(self.root.winfo_reqwidth() * 3))
        general_pane.add(explorer_pane)
        self.panes.append(explorer_pane)
        explorer_pane.add(tk.Label(explorer_pane, text="explorer pane"))

        console_pane = tk.PanedWindow(bd=2, orient=tk.VERTICAL, width=(self.root.winfo_reqwidth() * 3))
        general_pane.add(console_pane)
        self.panes.append(console_pane)
        console_pane.add(tk.Label(console_pane, text="console pane"))

        print((self.root.winfo_reqwidth()))

    def mainloop(self):
        self.root.mainloop()

    def create_label(self, pane_index, **kwargs):
        self.labels.append(tk.Label(self.panes[pane_index], kwargs))

    def add_label(self, pane_index, index, **kwargs):
        self.panes[pane_index].add(self.labels[index])

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

# class Frame(tk.Frame):

# def __init__(self):
