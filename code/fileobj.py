class FileObj : # TODO implement file class
    def __init__(self, name, content):
        self.name = name
        self.content = content
    def to_dict(self):
        if isinstance(self.content, str):
            return {self.name: self.content}
        dicti = {self.name: []}
        for i in self.content:
            dicti[self.name].append(i.to_dict())
        return dicti