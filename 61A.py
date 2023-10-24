# https://codeforces.com/problemset/problem/61/A
# Ultra-Fast Mathematician

line1 = str(input())
line2 = str(input())
output = []

for i in range(len(line1)):
  if line1[i] == line2[i]:
    output.append('0') 
  else:
    output.append('1')

print(''.join(output))
