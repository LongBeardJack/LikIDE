from window import Window
import config, importlib, traceback
lang = importlib.import_module("lang." + config.lang)

window = Window("Likide " + config.version + " (python: " + config.py_version + ")", "1080", "720")

if __name__ == "__main__":
    window.mainloop()
