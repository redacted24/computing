class Link():
    def __init__(self, nodes):
        self.nodea = nodes[0]
        self.nodeb = nodes[1]
        self.nodea_looped = None
        self.nodeb_looped = None
        self.weight = nodes[3]

    
    def whichNode(self, node):
        return self.nodea if node == self.nodea else self.nodeb
    
    def checkLoop(self, other, node):
        if self.whichNode():
            return True
        return False

    def loop(self, other, node):
        if node == self.nodeb:
            self.nodeb_looped = other.whichNode(self.nodeb_looped)
    
a = Link([1, 2, 15, 99])
b = Link([2, 3, 0, 100])

print(a.whichNode(2))
a.loop(b, 2)
print(a.nodeb_looped)