class Log:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        if parent is not None:
            self.parent.count += 1
            self.parent.children.append(self)
        self.content = ''

    def __delete__(self):
        if self.parent is not None:
            self.parent.count -= 1
            self.parent.children.remove(self)
        return

    def move(self, destination):
        if destination.count >= destination.lim:
            raise Exception('Destination folder is full')
            return
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
