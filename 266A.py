# https://codeforces.com/problemset/problem/266/A
# Stones on the Table

length = int(input())
user = list(str(input()))
moves = 0
count = 0

while count < length-1:
  for i in range(1, len(user[count:])):
    if user[count] == user[count+i]:
      user.pop(count+1)
      user.insert(count+1, '')
      count += 1
      moves += 1
  count += 1

print(moves)

  