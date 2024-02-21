length = int(input())
halved = length//2
content = []
number = 0
for i in range(length):
    content.append(input())

for i in range(halved):
    if content[i] == content[i+halved]:
        number += 1

print(number*2)
