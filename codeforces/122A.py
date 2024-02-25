number = int(input())
lucky = ['4', '7']

def isLucky(x):
    lucky = ['4', '7']
    for i in str(x):
        if not i in lucky:
            return False
    return True

def solver():
    if isLucky(number):
        return True
    else:
        for i in range(1, number):
            if number % i == 0:
                if isLucky(number//i) or isLucky(i):
                    return True


print('YES' if solver() else 'NO')

# Coherent with editorial