# https://codeforces.com/problemset/problem/510/A
# Fox and Snake

r, c = [int(x) for x in input().split()]

full = '#'*c
right = '.'*(c-1) + '#'
left = '#' + '.'*(c-1)

snake = [full, right, full, left]

count = 0

for i in range(r):
    if count > len(snake)-1:
        count = 0
    print(snake[count])
    count += 1

# Done