length = int(input())
coins = [int(x) for x in input().split()]
coins.sort(reverse=True)

def findMin():
    output = 1
    for i in range(1,length):
        if sum(coins[:i]) > sum(coins[i:]):
            return output
        output += 1
    return output
        

print(findMin())
