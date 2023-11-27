# https://codeforces.com/problemset/problem/268/A
# Games

user = int(input())
content = []

for i in range(user):
    content.append(input().split())

count = 0
for i in range(user):
    for j in range(user):
        if content[j][0] == content[i][1]:
            count += 1

print(count)

# Two Pointers for the win!