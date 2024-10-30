import json

class TaskParser:
    def __init__(self, task_to_parse):
        self.task_to_parse = task_to_parse

    def parse(self):
        return  json.load(self.task_to_parse)