# Question 3
n = int(input())
arr = str(input())
intArr = arr.split(' ')
count = 0

for i in range(n):
  intArr[i] = int(intArr[i])

for i in range(n):
  print(f'i: {i}')
  for j in range(i+1,n):
    print(f'j: {j}')
    if str(intArr[i]+intArr[j]) in arr:
      count += 1

print(count)
