class Puzzle:
    def __init__(self):
        a = input()
        self.word = [a, a[::-1]]
        self.height = int(input())
        self.table = []
        input()
        for i in range(self.height):
            content = ''.join(input().split(' '))
            self.table.extend([content])
        
        print(self.table)

    def checker(self, index, letter):
        if letter == self.word[0][index] or letter == self.word[1][index]:
            return True
        return False

    def findHorizontal(self):
        wordTrack = 0
        for row in self.table():
            for letter in row:
                if letter == a.checker(wordTrack, letter):
                    wordTrack += 1
                else:
                    wordTrack = 0

a = Puzzle()
