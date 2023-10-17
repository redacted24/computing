# Borze
# https://codeforces.com/problemset/problem/32/B

bruh = str(input())
borze = list(bruh)
output = ''
counter = 0

while counter < len(borze):
  if borze[counter] == '.':
    output += '0'
  elif borze[counter] == '-':
    if borze[counter+1] == '-':
      output += '2'
      counter += 1
    else:
      output += '1'
      counter += 1
  counter += 1

print(output)
