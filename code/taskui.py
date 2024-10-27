import os
from tkinter import *
from tkinter import ttk

from checker import Checker
from taskparser import TaskParser
from reverser import Reverser

class TaskUI:

    def set_step(self, step):
        self.checker.step = step
        self.reverser.reverse_to_step(step)
        self.current_step = step

    def __init__(self, task_number, root):
        frame = ttk.Frame(root)

        # Get Taski.txt
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(current_dir)
        task_dir = os.path.join(root_dir, 'Tasks')
        task_file_path = os.path.join(task_dir, f'Task{task_number}.txt')
        self.task_file = open(task_file_path)

        self.task_parser = TaskParser(self.task_file)

        self.tasks =self.task_parser.parse()
        self.current_step = 0

        self.checker = Checker(self.tasks, self.current_step)
        self.reverser = Reverser(self.tasks, self.current_step)

        ttk.Label(root, textvariable=self.tasks[self.current_step]).grid(column=0, row=0)

    def update_gui(self):
        pass
