content = []
days = {}

for i in range(5): # Set days dictionnary
    days[str(i+1)] = 0

number = int(input())

for i in range(number):
    a = input()
    content.append(a)

for i in range(5): #Moving days
    for j in range(number): #Moving people
        if content[j][i] == 'Y':
            days[str(i+1)] += 1


highest = max(sorted(days.values()))
out = ''

for key, val in days.items():
    if val == highest:
        out += (str(key) + ',')
    
print(out[:-1])

