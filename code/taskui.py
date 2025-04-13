import os
import shutil
from functools import partial
from tkinter import *
from tkinter import PhotoImage
from tkinter.messagebox import showinfo, showerror

from checker import Checker
from taskparser import TaskParser
from reverser import Reverser
from scrollframe import ScrollFrame

class TaskUI:
    def quit(self):
        self.frame.destroy()
        #self.cmd()
    def advance_step(self):
        if False not in self.completed:
            showinfo(message="Вы завершили урок!")
            quit()
        else:
            while self.completed[self.current_step]:
                self.current_step+=1
                self.current_step %= len(self.tasks)
                self.checker.step = self.current_step

        self.update_gui()
    def set_step(self, step):
        self.checker.step = step
        self.reverser.reverse_to_step(step)
        self.current_step = step
        self.update_gui()
    def resize_to_width(self, target_width, img):
        w = img.width()
        img = img.zoom(target_width, target_width)
        img = img.subsample(w,w)
        return img
    def __init__(self, task_number, root):
        root.tk_setPalette(background = "gray24")
        for widget in root.winfo_children():
            widget.destroy()
        #self.cmd = on_exit
        # Get Task1.json
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(current_dir)
        task_dir = os.path.join(root_dir, 'Tasks')
        if os.path.exists(os.path.join(root_dir, 'work')):
            shutil.rmtree(os.path.join(root_dir, 'work'))
        os.makedirs(os.path.join(root_dir, 'work'))
        os.startfile(os.path.join(root_dir, 'work'))
        task_file_path = os.path.join(task_dir, f'Task{task_number}.json')
        self.task_file = open(task_file_path, encoding = "utf-8-sig")

        self.task_parser = TaskParser(self.task_file)

        self.tasks =self.task_parser.parse()
        self.current_step = 0
        self.completed = [False for i in range(len(self.tasks))]

        self.checker = Checker(self.tasks, self.current_step)
        self.reverser = Reverser(self.tasks, self.current_step)

        self.frame = Frame(root)
        self.frame.pack(fill="both", expand=True)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)
        task_frame = Frame(self.frame, pady=5, padx=3)
        task_frame.grid(column=0, row = 0,sticky = "nwse")
        a_frame = ScrollFrame(self.frame)
        a_frame.grid(column=0, row=1, sticky="nwse")
        main_frame = Frame(a_frame.viewPort)
        main_frame.configure(bg = "white")
        main_frame.pack(fill = BOTH, side = LEFT)
        self.task_buttons = []
        self.task_description = Label(main_frame, text=self.tasks[self.current_step][0], wraplength=600, bg="white", fg="black", justify="left")
        self.img = PhotoImage(file = self.tasks[self.current_step][3]).subsample(1,1)
        self.task_image = Label(main_frame, image = self.img)
        self.lesson_label = Label(task_frame, text  = f"Урок №{task_number}", justify="right")
        self.check_button = Button(self.frame, text = "Проверить", command=self.check, bg = "lime green", fg = "black", relief=FLAT, borderwidth=0)
        for i in range(len(self.tasks)):
            cmd = partial( self.set_step, i)
            self.task_buttons.append(Button(task_frame, text = str(i+1), command=cmd, width = 2, fg = "black", borderwidth=0))
            self.task_buttons[i].grid(column = i, row = 0, sticky = "nw", padx = 1)
        task_frame.columnconfigure(len(self.tasks), weight = 1)
        self.task_description.grid(column = 0, row = 0, sticky = "nw")
        self.check_button.grid(column = 0, row = 2, sticky = "s", pady = 10)
        self.task_image.grid(column = 0, row = 1, sticky = "e")
        self.lesson_label.grid(column = len(self.tasks), row = 0, sticky = "e")
        self.update_gui()
        self.set_step(0)

    def update_gui(self):

        self.task_description.configure(text=self.tasks[self.current_step][0])
        self.img = PhotoImage(file = self.tasks[self.current_step][3]).subsample(1,1)
        self.task_image.configure(image=self.img)
        for i in range(len(self.tasks)):
            if not self.completed[i]:
                self.task_buttons[i].configure(bg = "dim gray", relief=FLAT)
            else:
                self.task_buttons[i].configure(bg = "lime green", relief=FLAT)
            if i == self.current_step:
                self.task_buttons[i].configure(bg = "white", relief=FLAT)
                if self.completed[i]:
                    self.task_buttons[i].configure(bg = "pale green", relief=FLAT)

    def check(self):

        if self.checker.check():
            self.completed[self.current_step] = True
            self.advance_step()
            showinfo(message="Поздравляю")
        else:
            showerror(message="Неверно")
