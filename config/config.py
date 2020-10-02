from platform import python_version
from os.path import expanduser

name = "likide"
version = "0.0.3"
py_version = python_version()
author = "BIPBIPGaminG & Tudiiii"
lang = "fr_FR"
font_size = "16"
font_family = "Segoe\ UI\ Light"
dir_var = {'DISK': "C", 'USER_HOME': expanduser("~")}
current_project_dir = '{USER_HOME}\\Documents\\Likide\\FirstProject\\'.format(**dir_var)
current_file_name = "../main.py"


background_color = "#4f4f4f"
foreground_color = "#eaeaea"
