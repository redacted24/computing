k = int(input())
word = input()
keys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
word_List = list(word)

for letter in range(len(word)):
  word_List[letter] = keys[keys.index(word[letter])+k]

word_List = ''.join(word_List)
print(word_List)
