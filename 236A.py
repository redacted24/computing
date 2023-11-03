# https://codeforces.com/problemset/problem/236/A
# Boy or Girl
# sevenkplus

name = str(input())
seen = []
count = 0

for i in name:
  if i in seen:
    continue
  else:
    seen.append(i)
    count += 1

if count % 2 == 0:
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")
