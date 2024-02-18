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
    
    def __repr__(self):
        '''Prints the number of words found'''
        return f'{str(self.count)} words found: {str(self.word)} table: {self.table}'

    def wordFinder(self, table_line):
        '''Main func to iterate through strings and find how many occurences of the substring appears'''
        self.count += table_line.count(self.word)
    
    def straight(self, table):
        '''Iterate through a table, straight forward direction'''
        for line in table:
            self.wordFinder(line)
        
    def inverse(self, table):
        '''Iterate through a table, reverse direction'''
        for line in table:
            self.wordFinder(line[::-1])
    
    def searchHorizontal(self):
        '''Search for horizontal'''
        self.straight(self.table)
        self.inverse(self.table)
    
    def searchVertical(self):
        '''Search for Vertical'''
        temp = []
        for j in range(self.width):
            tempstr = ''
            for i in range(self.height):
                tempstr += self.table[i][j]
            temp.append(tempstr)
        self.straight(temp)
        self.inverse(temp)
            
    def searchDiagonal(self):
        '''Search for Diagonals'''
        diag = [[] for _ in range(self.width + self.height -1)]
        bdiag = [[] for _ in range(len(diag))]
        min_diag = -self.width+1
        for x in range(self.height):
            for y in range(self.width):
                diag[x+y].append(self.table[x][y])
                bdiag[x-y-min_diag].append(self.table[y][x])

        self.straight(diag)
        self.inverse(diag)
        self.straight(bdiag)
        self.inverse(bdiag)


a = Puzzle()
a.searchHorizontal()
a.searchVertical()
a.searchDiagonal()
print(a)