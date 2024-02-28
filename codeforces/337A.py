n,m = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]
numbers.sort()
best = float('infinity')
# print(numbers)

for i in range(m-n+1):
    best = min(best, numbers[i+n-1]-numbers[i])
    # print('largest number:', numbers[i+n-1])
    # print('smallest number: ', numbers[i])
    # print(best, numbers[i+n-1]-numbers[i])

print(best)
