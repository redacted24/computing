# https://codeforces.com/problemset/problem/118/A
# String Task

vowels = ['a', 'o', 'e', 'i', 'y', 'u']

user = str(input()).lower()
user = list(user)


counter = 0
while counter < len(user):
    if user[counter] in vowels:
        user.pop(counter)
    else:
        counter += 1

counter = 0 

for i in range(len(user)):
    user.insert(i + counter, '.')
    counter += 1
user = ''.join(user)

if not user:
    user += '.'

print(user)




