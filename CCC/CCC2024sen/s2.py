content = [int(x) for x in input().split()]
sentences = []
for i in range(content[0]):
    sentences.append(input())

seen = {}
out = []

def check(ls):
    counter = 0
    for i in range(len(ls)-1):
        if ls[counter] == ls[counter+1]:
            return 'F'
        counter += 1
    return 'T'
        
for sentence in sentences:
    test = []
    for letter in sentence:
        seen[letter] = seen.setdefault(letter, 0) + 1
    for key, val in seen.items():
        if val == 1:
            seen[key] = 1
        else:
            seen[key] = 0
    for letter in sentence:
        test.append(seen[letter])
    out.append(check(test))
    seen.clear()

for i in out:
    print(i)
