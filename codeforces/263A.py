# A Beautiful Matrix
# https://codeforces.com/problemset/problem/263/A

t = 5
content = []
for i in range(t):
    contents = [int(x) for x in input().split(' ')]
    content.append(contents)

index1 = 0
moves = 0

for i in range(t):
    if sum(content[i]):
        index1 = i
moves += abs(index1-2)
moves += abs(content[index1].index(1)-2)
print(moves)

# Index starts from 0!!!!! So you need everything to be at index 2
