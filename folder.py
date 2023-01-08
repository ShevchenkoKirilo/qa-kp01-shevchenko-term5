class Folder:
    def __init__(self, name, lim=0, parent=None):
        self.name = name
        self.lim = lim
        self.parent = parent
        self.count = 0
        self.children = []
        if parent is not None:
            self.parent.count += 1
            self.parent.children.append(self)

    def __delete__(self):
        if self.parent is not None:
            self.parent.count -= 1
            self.parent.children.remove(self)
        return

    def list(self, space=''):
        result = ''
        for item in self.children:
            if type(item) is Folder:
                result += space + '->' + self.name + '\n'
                space += '  '
                result += item.list(space + '  ')
                result += space + '<-\n'
            else:
                result += space + item.name + ', ' + '\n'
        print(result)
        return result

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
