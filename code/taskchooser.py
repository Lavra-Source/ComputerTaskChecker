import os
import shutil
from functools import partial
from tkinter import *
from tkinter import PhotoImage
from tkinter.messagebox import showinfo, showerror
from taskui import TaskUI
TASK = -1
TASKCOOUNT = 2
root = Tk()
def exit_task():
    TASK = -1
    update_gui()
def update_gui():
    buttons = []
    for i in range(TASKCOOUNT):
        cmd = partial(jump_into_task, i + 1)
        buttons.append(Button(root, text=str(i + 1), command=cmd, width=2))
        buttons[i].grid(column=i, row=0, sticky="nw")
def init():
    global root
    root = Tk()
    root.title("Учебное пособие по информатике")
    root.geometry("1280x600")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    update_gui()
    root.mainloop()

def jump_into_task(task_number):
    TASK = task_number
    cmd = partial(exit_task)
    task = TaskUI(task_number, root, cmd)