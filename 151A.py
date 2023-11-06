# https://codeforces.com/problemset/problem/151/A
# Soft Drinking

output = []

data = [int(x) for x in input().split()]

drink = data[6]
slices = 1
salt = data[7]

avslices = data[3] * data[4]
avdrink = data[1] * data[2]
avslices = data[3] * data[4]
avsalt = data[5]



output.append(avdrink//drink)
output.append(avslices//slices)
output.append(avsalt//salt)

if 0 in output:
  print('0')
else:
  print(min(output)//data[0])
