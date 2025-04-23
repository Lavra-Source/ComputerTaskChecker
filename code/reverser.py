import shutil
import os

class Reverser:
    def create(self, d, file_path):
        if d["type"] == "file":
            with open(file_path, 'w', encoding = "utf-8") as file:
                # Write content to the file
                file.write(d["content"])
        else:

            os.makedirs(file_path)
            for i in d["children"]:
                new_path = os.path.join(file_path, i["name"])
                self.create(i, new_path)
    def __init__(self, tasks, step):
        self.tasks = tasks
        self.step = step
    def reverse_to_step(self, step):
        self.step = step
        current_dir = os.path.dirname(os.path.abspath(__file__))
        root_dir = os.path.dirname(current_dir)
        task_dir = os.path.join(root_dir, 'work')
        shutil.rmtree(task_dir, ignore_errors=False)
        self.create(self.tasks[step][1], task_dir)
        print(f"reversed to step {step}")

