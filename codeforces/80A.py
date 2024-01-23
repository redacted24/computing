# https://codeforces.com/problemset/problem/80/A
# Panoramix's Prediction

user = [int(x) for x in input().split()]
n, m = user[0], user[1]
temp = n+1

def findNextPrime(temp):
  """Find next prime"""
  while temp <= 50:
    for i in range(2, temp):
      if not (temp / i % 1):
        break
    else:
      return temp
    temp += 1

if findNextPrime(temp) == m:
  print('YES')
else:
  print('NO')
