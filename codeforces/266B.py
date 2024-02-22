x = [int(x) for x in input().split()]
line = [input()]
for i in line[0]:
    line.append(i)
line = line[1:]

for j in range(x[1]):
    pointer = 0
    while pointer < x[0]-1:
        if line[pointer] == 'B' and line[pointer+1] == 'G':
            line[pointer], line[pointer+1] = line[pointer + 1], line[pointer]
            pointer += 1
        pointer += 1

print(''.join(line))
