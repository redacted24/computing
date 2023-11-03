# https://codeforces.com/problemset/problem/231/A
# Team
content = []
final = 0
b = int(input())
for i in range(b):
  contents = [int(x) for x in input().split()]
  content.append(contents)

print(content)

for i in range(len(content)):
  if content[i].count(1) >= 2:
    final += 1

print(final)
  
