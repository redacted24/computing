length = int(input())
lot = [x for x in input().split()]

def check():
    out = []
    ls = []
    valid = True
    while valid:
        pointer = 0
        team = []
        while pointer < length:
            if not lot[pointer] in team and lot[pointer] != '':
                team.append(lot[pointer])
                lot[pointer] = ''
                ls.append(str(pointer+1))
            pointer += 1

        if len(ls) == 3:
            out.append(ls)
            ls = []
            continue
        
        valid = False
    
    if not out:
        return False
    else:
        return out

a = check()
if a:
    print(len(a))
    for i in a:
        print(' '.join(i))
else:
    print(0)
