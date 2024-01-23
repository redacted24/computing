# https://codeforces.com/problemset/problem/110/A
# Nearly Lucky Number

user = str(input())
counter = 0
for i in user:
  if i == '4' or i == '7':
    counter += 1
counter = str(counter)
for i in counter:
  if i == '4' or i == '7':
    continue
  else:
    print('NO')
    break
else:
  print('YES')

# You can use else at the end of a for statement to execute something after the successful completion of the floor loop