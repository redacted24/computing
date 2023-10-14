truth = str(input())
ek = str(input())

def boom(truth, ek):
  while ek in truth:
    truth = truth.replace(ek,'')
  if not truth:
    return 'EMPTY'
  return truth

output = boom(truth,ek)
print(output)

"""
12ab112ab2ab12ab
12ab

"""
