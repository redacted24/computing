# https://codeforces.com/problemset/problem/155/A
# I_love_%username%

a = int(input())
b = [int(x) for x in input().split()]
high = b[0]
low = b[0]
output = 0

for i in b:
    if i > high:
        output += 1
        high = i
    elif i < low:
        output += 1
        low = i
    else:
        continue

print(output)