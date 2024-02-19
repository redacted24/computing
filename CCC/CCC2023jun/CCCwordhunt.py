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
        return f'{str(self.count)}'

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
            
    def searchDiagonals(self):
        '''Search for Diagonals'''
        def topDown():
            '''Search diagonals from top to down'''
            output = []
            tempstr = []
            # Possible to simplify this into one while block?
            for i in range(self.width):
                heightPt = 0
                tempstr.append(self.table[heightPt][i])
                while heightPt < self.height-1 and i > 0:
                    heightPt += 1
                    i -= 1 
                    tempstr.append(self.table[heightPt][i])
                output.append(''.join(tempstr))
                tempstr = []
            
            for height in range(1,self.height):
                widthPt = self.width - 1
                tempstr.append(self.table[height][widthPt])
                while height < self.height-1:
                    height += 1
                    widthPt -= 1
                    tempstr.append(self.table[height][widthPt])
                output.append(''.join(tempstr))
                tempstr = []
            
            self.straight(output)
            self.inverse(output)
        
        def downTop():
            '''Search diagonals from down to top'''
            output = []
            tempstr = []
            for i in range(self.width):
                heightPt = self.height-1
                tempstr.append(self.table[heightPt][i])
                while heightPt > 0 and i > 0:
                    heightPt -= 1
                    i -= 1 
                    tempstr.append(self.table[heightPt][i])
                output.append(''.join(tempstr))
                tempstr = []
            
            for height in range(self.height-2, -1,-1):
                widthPt = self.width - 1
                tempstr.append(self.table[height][widthPt])
                while height > 0:
                    height -= 1
                    widthPt -= 1
                    tempstr.append(self.table[height][widthPt])
                output.append(''.join(tempstr))
                tempstr = []
            
            self.straight(output)
            self.inverse(output)

        topDown()
        downTop()

    def perpendiculars():
        '''Find word in perpendicular strings'''
        def straightPerpendiculars():
            '''Find word in all straight perpendicular strings'''
            

        def diagonalPerpendiculars():
            '''Find word in all diagonal perpendiculars'''
        
            

    def run(self):
        a.searchHorizontal()
        a.searchVertical()
        a.searchDiagonals()
        # a.perpendiculars()
                
a = Puzzle()
a.run()
print(a)
