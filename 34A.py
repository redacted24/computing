# https://codeforces.com/problemset/problem/34/A
# Reconnaissance 2

user = int(input())
content = [int(x) for x in input().split()]
minimum = float('infinity')
indexes = []

for i in range(0, user-1):
  comp = abs(content[i] - content[i+1])
  if comp < minimum:
    minimum = comp
    indexes = [i+1, i+2]

if abs(content[-1] - content[0]) < minimum:
  indexes = [len(content), 1]
  
print(indexes[0], indexes[1])
