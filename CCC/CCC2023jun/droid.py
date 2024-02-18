delivery = int(input())
collisions = int(input())

points = delivery*50 - collisions*10

if delivery > collisions:
    points += 500

print(points)