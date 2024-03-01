levels = int(input())
x = {int(x) for x in input().split()[1:]}
y = {int(x) for x in input().split()[1:]}

a = x.union(y)
if len(a) == levels:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')