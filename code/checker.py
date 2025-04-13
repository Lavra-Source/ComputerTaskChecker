import os
def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
    else:
        d['type'] = "file"
        d["content"] = open(path, 'r', encoding="utf-8-sig").read()

    return d
class Checker:

    def __init__(self, tasks, step):
        self.tasks = tasks
        self.step = step
        self.temp = True
    def check(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(current_dir)
        task_dir = os.path.join(root_dir, 'work')
        return path_to_dict(task_dir)==self.tasks[self.step][2]