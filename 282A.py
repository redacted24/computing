# https://codeforces.com/problemset/problem/282/A
# Bit ++ 

#Bitland!

user = int(input())
content = []
output = 0

for i in range(user):
    content.append(input())

for i in content:
    if '+' in i:
        output += 1
    else:
        output -= 1

print(output)