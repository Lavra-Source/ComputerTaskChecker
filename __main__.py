import site
import sys
from tkinter import *
from tkinter import ttk
site.addsitedir('./code')  # Always appends to end
print(sys.path)
from taskui import TaskUI

root = Tk()
root.title("Учебное пособие по информатике")
t_ui = TaskUI(1, root)
t_ui.update_gui()
root.mainloop()