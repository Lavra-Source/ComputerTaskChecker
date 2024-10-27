from fileobj import FileObj
class Reverser:
    def __init__(self, tasks, step):
        self.tasks = tasks
        self.step = step
    def reverse_to_step(self, step):
        print(f"reversed to step {step}") #TODO actually implement dis