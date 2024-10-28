import os
from functools import partial
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

from checker import Checker
from taskparser import TaskParser
from reverser import Reverser

class TaskUI:

    def advance_step(self):
        self.current_step+=1
        self.checker.step = self.current_step
        self.max_step = max(self.max_step, self.current_step)
        self.update_gui()
    def set_step(self, step):
        self.checker.step = step
        self.reverser.reverse_to_step(step)
        self.current_step = step
        self.update_gui()

    def __init__(self, task_number, root):


        # Get Taski.txt
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(current_dir)
        task_dir = os.path.join(root_dir, 'Tasks')
        task_file_path = os.path.join(task_dir, f'Task{task_number}.txt')
        self.task_file = open(task_file_path)

        self.task_parser = TaskParser(self.task_file)

        self.tasks =self.task_parser.parse()
        self.current_step = 0
        self.max_step = 0

        self.checker = Checker(self.tasks, self.current_step)
        self.reverser = Reverser(self.tasks, self.current_step)

        root.columnconfigure(0, weight=1)

        frame = ttk.Frame(root)
        frame.grid(column=0, row=0)

        frame.columnconfigure(0, weight=1)
        task_frame = ttk.Frame(frame)
        task_frame.grid(column=0, row = 0)

        self.task_buttons = []
        self.task_description = ttk.Label(frame, text=self.tasks[self.current_step][0])
        self.check_button = ttk.Button(frame, text = "Проверить", command=self.check)
        for i in range(len(self.tasks)):
            cmd = partial( self.set_step, i)
            self.task_buttons.append(ttk.Button(task_frame, text = str(i+1), command=cmd, width = 2))
            self.task_buttons[i].grid(column = i, row = 0)

        self.task_description.grid(column=0, row = 1)
        self.check_button.grid(column = 0, row = 2)
        self.update_gui()

    def update_gui(self):
        self.task_description.configure(text=self.tasks[self.current_step][0])
        for i in range(len(self.tasks)):
            if i > self.max_step:
                self.task_buttons[i].configure(state="disabled")
            else:
                self.task_buttons[i].configure(state="normal")
            if i == self.current_step:
                self.task_buttons[i].configure(state="active")

    def check(self):
        if self.checker.check():
            self.advance_step()
            showinfo(message="Поздравляю")
        else:
            showerror(message="Неверно")
