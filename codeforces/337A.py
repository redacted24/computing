n,m = [int(x) for x in input().split()]
numbers = [int(x) for x in input().split()]

numbers.sort()
print(numbers)

pointA = 0
pointB = 1
smallest = 1001

while pointB < len(numbers) and pointA < len(numbers)-1:
    a = numbers[pointB] - numbers[pointA]
    if a <= smallest and a != 0:
        smallest = a
        pointB += 1
    pointA += 1

print(smallest)
