class Binary:
    def __init__(self, name, content=None, parent=None):
        self.name = name
        self.content = content
        self.parent = parent
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
