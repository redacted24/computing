# https://codeforces.com/problemset/problem/116/A
# Tram
content = []
a = int(input())
otb = 0
maximum = 0

for i in range(a):
    content.append([int(x) for x in input().split()])

for i in range(a):
    otb -= content[i][0]
    if otb > maximum:
        maximum = otb
    otb += content[i][1]
    if otb > maximum:
        maximum = otb

print(maximum)

    
