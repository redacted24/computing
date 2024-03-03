n,k = [int(x) for x in input().split()]

def solver():
    def mid(k,n):
        if n % 2 == 0:
            if k > n//2:
                return [True, k-n//2]
            return [False,k]
        else:
            if k > (n//2)+1:
                return [True, k-(n//2)-1]
            return [False,k]
        
    a = mid(k,n)

    if a[0]:
        return a[1]*2
    else:
        return a[1]*2-1

print(solver())