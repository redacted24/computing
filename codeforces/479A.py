content = []
for i in range(3):
    content.append(int(input()))

a,b,c = content
biggest = max(a*b*c, (a+b)*c, a+(b*c), a*(b+c), (a*b)+c, a+b+c)

print(biggest)
