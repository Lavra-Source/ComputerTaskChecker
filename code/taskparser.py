from fileobj import FileObj
class TaskParser:
    def __init__(self, task_to_parse):
        self.task_to_parse = task_to_parse


    def parse(self):
        return  [[str(i), FileObj("hello", "hello")] for i in range(10)] #TODO actually implement dis