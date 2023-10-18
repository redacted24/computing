# Lights out
# https://codeforces.com/problemset/problem/275/A

# Assign variables and create empty solved matrix
row1 = [int(x) for x in input().split(' ')]
row2 = [int(x) for x in input().split(' ')]
row3 = [int(x) for x in input().split(' ')]

matrix = [row1, row2, row3]

solved = [
  [True, True, True, True, True],
  [True, True, True, True, True],
  [True, True, True, True, True],
  [True, True, True, True, True],
  [True, True, True, True, True]
]

# Algorithm
for i in range(3):
  for j in range(3):
    if matrix[i][j] % 2 != 0:
      solved[i][j+1] = not solved[i][j+1]
      solved[i+1][j+1] = not solved[i+1][j+1]
      solved[i+1][j] = not solved[i+1][j]
      solved[i+1][j+2] = not solved[i+1][j+2]
      solved[i+2][j+1] = not solved[i+2][j+1]
    else:
      continue

# Change list of booleans to print 0 and 1s
solved = [solved[1][1:4], solved[2][1:4], solved[3][1:4]]
solved = [[int(x) for x in solved[0]], [int(x) for x in solved[1]], [int(x) for x in solved[2]]]
solved = [[str(x) for x in solved[0]], [str(x) for x in solved[1]], [str(x) for x in solved[2]]]
solved = [''.join(solved[0]), ''.join(solved[1]), ''.join(solved[2])]
solved = '\n'.join(solved)

print(solved)
