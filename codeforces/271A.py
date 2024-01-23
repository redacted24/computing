# Beautiful Year
# https://codeforces.com/problemset/problem/271/A

year = int(input())

def search(x):
  '''
  Checks if a year number only has distinct digits. Returns True if yes, returns false if no. '''
  temp = list(str(x))
  for i in range(len(temp)-1):
    if temp[i] in temp[i+1:]:
      return False
  return True

def counting(x):
  '''Returns the year that is greater than the input, with only distinct digits'''

  while True:
    x += 1
    if search(x):
      return x

print(counting(year))

# Errors: 
# - on line 12, you wrote if i in temp[i+1], but that is simply comparing the i value! You need the value of temp at index i.
# - also, if the input is 9000, your previous program couldn't find it simply because the while loop had a restriction. Remember, the input has to be less than 9000, but the output doesn't need to!
