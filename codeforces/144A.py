# https://codeforces.com/problemset/problem/144/A
# Arrival of the General


# Input
t = int(input())
content = [int(x) for x in input().split()]

# Define the number of moves, which is the biggest number and which is the smallest number
moves = 0
big = 0
small = float('infinity')

for i in range(len(content)):
  if content[i] > big:
    big = content[i]

poppers = content.index(big)

content.pop(poppers)
content.insert(0, big)
moves += poppers

for i in range(len(content)):
  if content[i] < small:
    small = content[i]

def rindexList(list, value):
  """Find last occurance of smallest integer in the list. Acts as the index method of strings, but for lists. This is for cases where the different people have the same height."""
  return len(list)-list[::-1].index(value)

# Find the difference between last index and the index that the smallest height is currently at, then add that to the number of moves.
moves += len(content)-rindexList(content, small)

print(moves)
