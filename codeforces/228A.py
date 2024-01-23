# https://codeforces.com/problemset/problem/228/A
# Is your horseshoe on the other hoof?

content = [int(x) for x in input().split()]
buys = 0
y = []
for i in range(len(content)):
  if content[i] in y:
    buys += 1
  y.append(content[i])
print(buys)

# Make sure you are computing with integers, not strings! Large integers may be represented with scientific notation, and thus won't work with comparisons.
# Make a kind of memory of interated variables, cause otherwise your program wouldn't recognize the second 2 in 1 2 3 2. Here the memory is defined as y, nice
# When you iterate and to the len-1, careful of using other methods as if the loop iterates through everything.