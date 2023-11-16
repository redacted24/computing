info = [int(x) for x in input().split()]
sentence = list(input().split())
length = 0
output = []

for i in sentence:
  length += len(i)
  if length < info[1]:
    output.append(i)
  elif length == info[1]:
    output.append(i)
    print(' '.join(output))
    output = []
    length = 0
  else:
    print(' '.join(output))
    output = []
    length = len(i)
    output.append(i)
if output:
  print(' '.join(output))

# To help: you should reread the question, and layout a skeleton for it. Try to translate word to code first, before implementing your own code.
    









# limit = info[1]
# length = 0
# count = 0
# output = []

# for count in range(info[0]):
#   if length + len(sentence[count]) < limit:
#     output.append(sentence[count])
#     length += len(sentence[count])

#   else:
#     print(" ".join(output))
#     output = []
#     output.append(sentence[count])
#     length = len(sentence[count])
