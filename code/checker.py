from fileobj import FileObj

class Checker:

    def __init__(self, tasks, step):
        self.tasks = tasks
        self.step = step
        self.temp = True
    def check(self):
        self.temp = not self.temp #TODO actually implement this
        return self.temp