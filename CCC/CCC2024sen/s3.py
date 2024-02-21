length = int(input())
top = [x for x in input().split()]
bot = [x for x in input().split()]


def solver():
    def ordered(ls):
        '''Print ordered numbers in a string'''
        seen = []
        checking = ''
        for i in range(len(ls)):
            if ls[i] != checking:
                seen.append(ls[i])
                checking = ls[i]  
        return ''.join(seen)
    
    def samelmao(ls):
        temp = []
        for i in ls:
            if not i in temp:
                temp.append(i)
        return ''.join(temp)
    
    def sameOrder(t, b):
        temp = []
        for i in samelmao(t):
            if i in b:
                temp.append(i)
        # for i in ordered(t):
        #     if i in b:
        #         temp.append(i)
        if ''.join(temp) == samelmao(b):
            return True
        return False

    
    for i in bot:
        if not i in top:
            return 'NO'

    if top == bot:
        return 'YES\n0'

    elif sameOrder(top, bot):
        startShift = 0
        endShift = 0
        moveCounter = 0
        moves = []
        shifter = ''
        out = ''
        for i in range(length):
            if top[i] == bot[i]:
                continue
            else:
                startShift = i
                shifter = bot[i]
                if shifter in top[i:]:
                    while top[i] != shifter:
                        top[i] = shifter
                        i += 1
                    endShift = i
                    moveCounter += 1
                    moves.append(['L', str(startShift), str(endShift)])
                

        for i in range(length-1,-1,-1):
            if top[i] == bot[i]:
                continue
            else:
                startShift = i
                shifter = bot[i]
                while top[i] != shifter:
                    top[i] = shifter
                    i -= 1
                endshift = i
                moveCounter += 1
                moves.append(['R', str(endshift), str(startShift)])

        out += 'YES\n'
        out += str(moveCounter)
        for i in moves:
            r = ' '.join(i)
            out += '\n'
            out += r
        return out
    else:
        return 'NO'

print(solver())
