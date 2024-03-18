def solver():
    strength, duels = [int(x) for x in input().split()]
    fights = []
    for i in range(duels):
        fights.append([int(x) for x in input().split()])
    
    fights.sort(key=lambda x:x[0])
    
    for fight in fights:
        if strength > fight[0]:
            strength += fight[1]
        else:
            return 'NO'
    return 'YES'
        
print(solver())
