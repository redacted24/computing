# https://codeforces.com/problemset/problem/69/A?csrf_token=509b891c25c358b7b0af9b6d2dc7dc1f

t = int(input())
content = []
for i in range(t):
    contents = [int(x) for x in input().split(' ')]
    content.append(contents)

sumX = 0
sumY = 0
sumZ = 0

for i in range(t):
    sumX += content[i][0]
    sumY += content[i][1]
    sumZ += content[i][2]

if any([sumX, sumY, sumZ]):
    print('NO')
else:
    print('YES')
