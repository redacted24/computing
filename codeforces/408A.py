# https://codeforces.com/problemset/problem/408/A
# Line to Cashier

minTime = float('infinity')
content = []
cashes = int(input())
people = [int(x) for x in input().split()]
for i in range(cashes):
    a = [int(x) for x in input().split()]
    s = int(sum(a)*5)+len(a)*15
    if s < minTime:
        minTime = s

print(minTime)

# Done