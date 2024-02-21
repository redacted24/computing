# Take 2

class Puzzle:
    def __init__(self):
        self.word = input()
        self.height = int(input())
        self.table = []
        self.count = 0
        self.width = int(input())
        for i in range(self.height):
            content = ''.join(input().split(' '))
            self.table.extend([content])
    
    def checkTable(self):
        return self.table

    def finder(self):
        for row in range(self.height):
            for letter in self.table[row]:
                if letter == self.word[0]:
                    print(letter)


a = Puzzle()
a.finder()
print(a.checkTable())
