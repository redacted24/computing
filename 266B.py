# Queue at school
# https://codeforces.com/problemset/problem/266/B

t = [int(x) for x in input().split(' ')]
queue = list(input())
time = t[1]
counter = 0

while counter < len(queue):
  if queue[counter] == 'B':
    index = queue.index('B')
    queue.pop(index)
    queue.insert(index+1, 'B')
    counter += 1
  counter += 1
    


print(queue)
