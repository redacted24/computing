grid = [int(x) for x in input().split()]
moves = 0
ls = []

for x in range(1,grid[1]+1):
    for y in range(1,grid[0]+1):
        ls.append((x,y))

while ls:
    removed = ls.pop()
    moves += 1
    if ls:
        i = 0
        while i < len(ls):
            if ls[i][0] == removed[0] or ls[i][1] == removed[1]:
                ls.pop(i)
                continue
            i += 1
if moves % 2 == 0:
    print('Malvika')
else:
    print('Akshat')
