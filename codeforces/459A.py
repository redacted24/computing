def solver():
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    if x1 == x2:
        side = abs(y2-y1)
        out = [x1+side, y1, x2+side, y2]
    elif y1 == y2:
        side = abs(x2-x1)
        out = [x1, y1+side, x2, y2+side]
    elif abs(x2-x1) == abs(y2-y1):
        side = abs(y2-y1)
        if y2 > y1:
            out = [x1, y1+side, x2, y2-side]
        else:
            out = [x1, y1-side, x2, y2+side]
    else:
        return [-1]
    return out

for i in solver():
    print(i, end=' ')