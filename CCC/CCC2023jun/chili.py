scale = {
    'Poblano': 1500,
    'Mirasol': 6000,
    'Serrano': 15500,
    'Cayenne': 40000,
    'Thai': 75000,
    'Habanero': 125000
}

peppers = []
total = 0
number = int(input())

for i in range(number):
    content = input()
    peppers.append(content)

for i in peppers:
    total += scale[i]

print(total)