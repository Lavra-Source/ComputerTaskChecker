import os
import shutil
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
        if self.max_step == len(self.tasks):
            self.max_step-=1
            self.current_step-=1
            showinfo(message="Вы завершили урок!")
            quit()
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
        if os.path.exists(os.path.join(root_dir, 'work')):
            shutil.rmtree(os.path.join(root_dir, 'work'))
        os.makedirs(os.path.join(root_dir, 'work'))
        os.startfile(os.path.join(root_dir, 'work'))
        task_file_path = os.path.join(task_dir, f'Task{task_number}.json')
        self.task_file = open(task_file_path)

        self.task_parser = TaskParser(self.task_file)

        self.tasks =self.task_parser.parse()
        self.current_step = 0
        self.max_step = 0

        self.checker = Checker(self.tasks, self.current_step)
        self.reverser = Reverser(self.tasks, self.current_step)
        s = ttk.Style()
        s.configure('Correct.TButton', background='green')

        frame = ttk.Frame(root, padding=[5,5,5,10])
        frame.pack(fill="both", expand=True)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)
        task_frame = ttk.Frame(frame, relief=RAISED, padding=[2,1,2,1])
        task_frame.grid(column=0, row = 0,sticky = "nwse")

        self.task_buttons = []
        self.task_description = ttk.Label(frame, text=self.tasks[self.current_step][0])
        self.check_button = ttk.Button(frame, text = "Проверить", command=self.check)
        for i in range(len(self.tasks)):
            cmd = partial( self.set_step, i)
            self.task_buttons.append(ttk.Button(task_frame, text = str(i+1), command=cmd, width = 2))
            self.task_buttons[i].grid(column = i, row = 0, sticky = "nw")

        self.task_description.grid(column=0, row = 1, sticky = "nw")
        self.check_button.grid(column = 0, row = 2, sticky = "s")
        self.update_gui()
        self.set_step(0)

    def update_gui(self):

        self.task_description.configure(text=self.tasks[self.current_step][0])
        for i in range(len(self.tasks)):
            if i > self.max_step:
                self.task_buttons[i].configure(state="disabled")
            else:
                self.task_buttons[i].configure(state="normal")
            if i == self.current_step:
                self.task_buttons[i].configure(style = "TButton")

    def check(self):

        if self.checker.check():
            self.advance_step()
            showinfo(message="Поздравляю")
        else:
            showerror(message="Неверно")
