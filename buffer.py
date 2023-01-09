class Buffer:
    def __init__(self, name, size=0, parent=None):
        self.name = name
        self.size = size
        self.parent = parent
        if parent is not None:
            self.parent.count += 1
            self.parent.children.append(self)
        self.content = []

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

    def push(self, content):
        if len(self.content) >= self.size:
            raise Exception('Buffer is full')
        self.content.append(content)
        return

    def consume(self):
        if len(self.content) > 0:
            result = self.content[0]
            self.content.pop(0)
            return result
        return None
