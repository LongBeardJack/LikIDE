import tkinter as tk
from tkinter import font
import config
import importlib
import os
from tkinter.filedialog import askopenfile
from fileNamePopup import FileNamePopup
from fileSavePopup import FileSavePopup
import time

lang = importlib.import_module("lang." + config.lang)


class Window:
    EDITOR = 0
    EXPLORER = 1
    CONSOLE = 2

    root = None
    panes = []
    labels = []
    buttons = []
    editor_area = None
    file_text = None

    def donothing(self):
        pass

    def change_theme(self):
        if config.background_color is "#4f4f4f":
            config.background_color = "#c5c5c5"
            config.foreground_color = "#2d2d2d"
        else:
            config.background_color = "#4f4f4f"
            config.foreground_color = "#eaeaea"
        self.update(config.background_color, config.foreground_color)

    def __init__(self, title="Title", width="300", height="300"):
        self.root = tk.Tk()

        self.file_text = tk.StringVar()
        self.root.geometry(str(width) + "x" + str(height))
        self.root.title(title)

        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label=lang.new, command=lambda: self.create_new_file())
        file_menu.add_command(label=lang.open, command=lambda: self.open_file())
        file_menu.add_command(label=lang.save, command=lambda: self.donothing)
        file_menu.add_separator()
        file_menu.add_command(label=lang.exit, command=lambda: self.root.destroy())
        menu_bar.add_cascade(label=lang.file_menu, menu=file_menu)

        menu_bar.add_command(label=lang.run, command=lambda: self.donothing)

        apparence_menu = tk.Menu(menu_bar, tearoff=0)
        apparence_menu.add_command(label=lang.dark_theme, command=lambda: self.change_theme())
        apparence_menu.add_command(label=lang.light_theme, command=lambda: self.change_theme())
        menu_bar.add_cascade(label=lang.apparence_menu, menu=apparence_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="Help Index", command=lambda: self.donothing)
        help_menu.add_command(label=lang.about, command=lambda: self.donothing)
        menu_bar.add_cascade(label=lang.help_menu, menu=help_menu)

        self.root.config(menu=menu_bar)

        general_pane = tk.PanedWindow(bg=config.background_color)
        general_pane.option_add('*Font', config.font_family, config.font_size)
        general_pane.pack(fill=tk.BOTH, expand=1)

        editor_pane = tk.PanedWindow(bd=1, orient=tk.HORIZONTAL, width=((self.root.winfo_reqwidth() * 3) * 2))
        general_pane.add(editor_pane)
        self.panes.append(editor_pane)
        self.editor_area = tk.Text(editor_pane, bg=config.background_color, fg=config.foreground_color)
        editor_pane.add(self.editor_area)

        explorer_pane = tk.PanedWindow(bd=2, orient=tk.VERTICAL, width=(self.root.winfo_reqwidth() * 3))
        general_pane.add(explorer_pane)
        self.panes.append(explorer_pane)
        explorer_pane.add(tk.Label(explorer_pane, text="explorer pane"))

        console_pane = tk.PanedWindow(bd=2, orient=tk.VERTICAL, width=(self.root.winfo_reqwidth() * 3))
        general_pane.add(console_pane)
        self.panes.append(console_pane)
        console_pane.add(tk.Label(console_pane, text="console pane"))

    def open_file(self):
        text = askopenfile(parent=self.root).read()
        self.editor_area.delete("1.0", tk.END)
        self.editor_area.insert(tk.END, text)

    def create_new_file(self):
        if os.path.isdir(config.current_project_dir) is False:
            os.makedirs(config.current_project_dir)

        popup = FileNamePopup()
        popup.mainloop()

        if self.editor_area is not None and self.editor_area.get("1.0", tk.END) is not None:
            save = self.save_popup()

            if save == 0:
                f = open(config.current_project_dir + config.current_file_name, "w")
                f.write(self.editor_area.get("1.0", tk.END))
                f.close()
            elif save == 2:
                return
            else:
                pass

        f = open(config.current_project_dir + popup.get_name(), "w+")
        config.current_file_name = popup.get_name()
        self.editor_area.delete("1.0", tk.END)
        self.editor_area.insert(tk.END, f.read())
        f.close()

    def save_popup(self):
        popup = FileSavePopup()
        popup.mainloop()

        return popup.get_choice()

    def update(self, bg, fg):
        self.editor_area.config(bg=bg, fg=fg)

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
