# n total ride, m special ticket rides, cost of 1 normal ticket, cost of special ticket

n,m,a,b = [int(x) for x in input().split()]

def solver():
    if a*m > b:
        remainder = n % m
        if remainder == 0:
            return (n//m)*b
        else:
            if remainder*a <= b:
                return (n//m)*b+remainder*a
            else:
                return (n//m+1)*b
    else:
        return (n*a)

print(solver())