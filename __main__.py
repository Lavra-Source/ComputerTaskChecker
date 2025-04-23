import site
import sys
from functools import partial
from tkinter import *
from tkinter import ttk
site.addsitedir('./code')  # Always appends to end
print(sys.path)
from taskui import TaskUI
sys.stdin.reconfigure(encoding='utf-8-sig')
sys.stdout.reconfigure(encoding='utf-8-sig')
root = Tk()
root.title("Файлик")
root.geometry("1280x600")
s = ttk.Style()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
t_ui = TaskUI(1, root)
t_ui.update_gui()
root.mainloop()
