def find():
    word = 'hello'
    user = input()
    counter = 0
    i = 0
    while counter < len(word) and i < len(user):
        if user[i] == word[counter]:
            counter += 1
        i += 1
    return 'YES' if counter == len(word) else 'NO'

print(find())
