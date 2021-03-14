import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = 'win32GUI'

os.environ['TCL_LIBRARY'] = r"C:\Users\91995\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6"
os.environ['TK_LIBRARY']  = r"C:\Users\91995\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6"

executables = [cx_Freeze.Execuatbles("textPad.py", base=base, icon='icon.ico')]


cx_Freeze.setup(
    name = 'textPad Text Editor',
    options = {"build.exe": {"packages":["tkinter", "os"], "include_files":["icon.ico", "tcl86t.dll", "tk86t.dll", "icons2"]}},
    version = "0.01",
    description = 'Tkinter Application',
    executables = executables
)