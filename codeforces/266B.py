# Queue at school
# https://codeforces.com/problemset/problem/266/B

x = [int(x) for x in input().split()]
line = str(input())
temp = ''
seconds = x[1]
people = x[0]
i = 0

for j in range(seconds):
  print("Running loop")
  while i < people:
    if line[i+1] == 'G' and line[i] == 'B':
      temp += 'GB'
      i += 2
    else:
      temp += line[i]
      i += 1
      print(temp, i)

  # reset
  line = temp
  i = 0

print(temp)
