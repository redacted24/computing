string = input()

def solver():
    output = []
    tempstr = []
    i = 0
    while i < len(string):
        if string[i:i+3] == 'WUB':
            if tempstr:
                output.append(''.join(tempstr))
                tempstr.clear()
            i += 3
            continue
        else:
            tempstr.append(string[i])
            i += 1
    output.append(''.join(tempstr))
    return ' '.join(output)

print(solver())

# Shoulda removed both occurences
