# Queue at school
# https://codeforces.com/problemset/problem/266/B

t = [int(x) for x in input().split(' ')]
queue = list(input())
time = t[1]
output = queue[:]
print(f'Queue: {queue}, t = {t}')

for i in range(len(queue)):
    if queue[i] == 'B':
        index = queue.index('B')
        output.pop(index)
        output.insert(index+time, 'B')


print(output)
