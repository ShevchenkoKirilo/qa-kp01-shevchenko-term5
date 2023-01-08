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

    def list(self, tab=' '):
        result = ''
        result += tab + self.name + "\n"
        result += tab + "->\n"
        for child in self.children:
            if type(child) is Folder:
                tab += '   '
                result += child.list(tab)
                tab = tab[:-3]
            else:
                result += tab + '   ' + child.name + "\n"
        result += tab + "<-\n"
        return result

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
