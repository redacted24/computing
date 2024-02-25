length = input()
content = [int(x) for x in input().split()]

d1 = {}
out = []

counter = 1
for i in content:
    d1[i] = str(counter)
    counter += 1
for key in sorted(d1):
    out.append(d1[key])

print(' '.join(out))