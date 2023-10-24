# https://codeforces.com/problemset/problem/266/A
# Stones on the Table

length = int(input())
user = list(str(input()))
moves = 0
count = 0
newL = length - 1

while count < newL:
  if user[count] == user[count+1]:
    user.pop(count+1)
    newL -= 1
    moves += 1
  else:
    count += 1

print(moves)

# Key point here was to stay on an index as long as it is equal to the previous index. (so don't put count += 1 in the if statement)