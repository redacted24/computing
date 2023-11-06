# https://codeforces.com/problemset/problem/133/A
# HQ9+

user = str(input())
for i in user:
  if any([i == 'H', i == 'Q', i == '9']):
    print("YES")
    break
else:
  print("NO")
