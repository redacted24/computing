# https://codeforces.com/problemset/problem/248/A
# Cupboards

inputLength = int(input())
content = []
temp = []
arranged = []
row1 = 0
seconds = 0

for i in range(inputLength):
  content.append([int(x) for x in input().split()])

# Flipping horizontal list to 2 verical lists
for i in range(2):
  for j in range(len(content)):
    temp.extend([content[j][i]])
  arranged.append(temp)
  temp = []

# Check if a column has more zeros or ones. For either one that is bigger, return the number of the other (which is the shortest amount of seconds to flip cupboards so that all cupboards on one side are the same).
for i in range(2):
  for j in range(inputLength):
    if arranged[i][j] == 0:
      row1 += 1
  if row1 < inputLength/2:
    seconds += row1
  else:
    seconds += (inputLength-row1)
  row1 = 0

print(seconds)
