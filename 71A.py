# https://codeforces.com/problemset/problem/71/A
# Way Too Long Words

length = int(input())
content = []
output = []

def between(word):
  new = word[:]
  return str(len(new[1:-1]))

for i in range(length):
  content.append(input())
  if len(content[i]) > 10:
    b = [content[i][0], between(content[i]), content[i][-1]]
    content[i] = ''.join(b)

for i in range(len(content)):
  print(content[i])
