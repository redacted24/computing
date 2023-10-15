# Queue at school
# https://codeforces.com/problemset/problem/266/B

t = [int(x) for x in input().split(' ')]
queue = list(input())
time = t[1]

for i in range(len(queue)):
  if queue[i] == 'B':
    index = queue.index('B')
    queue.pop(index)
    queue.insert(index+1, 'B')
    


print(queue)
