from converter import path_to_dict
import os

class Checker:

    def __init__(self, tasks, step):
        self.tasks = tasks
        self.step = step
        self.temp = True
    def check(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(current_dir)
        task_dir = os.path.join(root_dir, 'work')
        return path_to_dict(task_dir)==self.tasks[self.step][1]