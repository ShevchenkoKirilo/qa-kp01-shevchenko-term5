class Log:
    def __init__(self, name, parent=None, content=''):
        self.name = name
        self.parent = parent
        self.content = content
        if parent is not None:
            self.parent.count += 1
            self.parent.children.append(self) 

    def __delete__(self):
        if self.parent is not None:
            self.parent.count -= 1
            self.parent.children.remove(self)
        return

    def move(self, destination):
        if destination.count >= destination.lim:
            raise Exception('Destination folder is full')
        if self.parent is not None:
            self.parent.count -= 1
            self.parent.children.remove(self)
        self.parent = destination
        self.parent.children.append(self)
        self.parent.count += 1
        return

    def readfile(self):
        return self.content

    def append(self, content):
        self.content += content + "\n"
        return 
