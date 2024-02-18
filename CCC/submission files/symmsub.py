length = int(input())
aaa = [int(x) for x in input().split()]

def solve(mountains):

    def asym(sublist):
        if len(sublist) == 1:
            return 0
        t1 = 0
        t2 = len(sublist)-1
        sums = []
        while t1 < t2:
            if t1 == t2:
                return 0
            sums.append(abs(sublist[t1]-sublist[t2]))
            t1 += 1
            t2 -= 1

        return sum(sums)
    
    maxi = []

    for size in range(length):
        sub = []
        p1 = 0
        p2 = 0 + size
        while p2 != length:
            sub.append(asym(mountains[p1:p2+1]))
            p1 += 1
            p2 += 1
        
        maxi.append(min(sub))

    out = ''
    for i in maxi:
        out += str(i) + ' '
    return out

print(solve(aaa))