# Word
# https://codeforces.com/problemset/problem/59/A

user = str(input())
out = ''
upperCount = 0
lowerCount = 0

for i in user:
  if i.isupper():
    upperCount += 1
  else:
    lowerCount += 1

if upperCount < lowerCount or upperCount == lowerCount:
  print(user.lower())
elif upperCount > lowerCount:
  print(user.upper())
