# https://codeforces.com/problemset/problem/144/A
# Arrival of the General

t = int(input())
content = [int(x) for x in input().split()]
moves = 0
big = 0
small = float('infinity')

for i in range(len(content)):
  if content[i] > big:
    big = content[i]

poppers = content.index(big)

content.pop(poppers)
moves += poppers

for i in range(len(content)):
  if content[i] < small:
    small = content[i]

moves += (len(content)-1)-content.index(moves)

print(moves)
