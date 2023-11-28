# https://codeforces.com/problemset/problem/443/A
# Anton and Letters

words = str(input()).strip('{}').split(', ')
seen = ['']
output = 0
for i in words:
  if i in seen:
    continue
  else:
    seen.append(i)
    output += 1

print(output)

# Accepted