length = int(input())
content = [int(x) for x in input().split()]

ls = list(range(length))

for index, val in enumerate(content):
    ls[val-1] = str(index+1)

print(' '.join(ls))