# https://cccgrader.com/getproblem.php?fid=928098&authcode=80934a4107f558d515981948eb06ba38
# 1 2 3 4 5 6 7 8 9

"""
Tests:

Input 1:
7
3 1 4 1 5 9 2

Input 2:
4
1 3 5 6


"""

# length = 7
# aaa = [3, 1, 4, 1, 5, 9, 2]

length = int(input())
aaa = [int(x) for x in input().split()]

def solve(mountains):

    def asym(sublist):
        # print(f'sublist fed into asym func: {sublist} length: {len(sublist)}')
        if len(sublist) == 1:
            return 0
        t1 = 0 #sublist[0] beginning
        t2 = len(sublist)-1 # equivalent of sublist[-1]
        sums = []
        while t1 < t2: # Avoids pointers crossing each other
            if t1 == t2:
                return 0
            sums.append(abs(sublist[t1]-sublist[t2]))
            # print(f'asym found: {abs(sublist[t1]-sublist[t2])}\n')
            t1 += 1
            t2 -= 1

        return sum(sums)
    
    maxi = []

    for size in range(length):
        sub = []
        p1 = 0
        p2 = 0 + size
        while p2 != length:
            # print(f'iterating...: {mountains[p1:p2+1]}')
            sub.append(asym(mountains[p1:p2+1]))
            p1 += 1
            p2 += 1
        
        maxi.append(min(sub))
        # print(f'minimum found: {min(sub)}, moving on to next length\n')

    # Turn to string
    out = ''
    for i in maxi:
        out += str(i) + ' '
    return out

print(solve(aaa))


# for scan_length in range(1, length+1):
#     while end_pointer <= len(mountains)-1:
#         temp = mountains[start_pointer:start_pointer+scan_length-1]
#         a = start_pointer
#         b = end_pointer

#         # Determine how many steps to "close" a crop
#         if scan_length % 2 == 0:
#             steps = scan_length // 2
#         elif scan_length == 1:
#             steps = 1
#         else:
#             steps = (scan_length) // 2 + 1

#         # Calculate the asymmetric value
#         for j in range(steps):
#             sub.append(abs(temp[a]-temp[b]))
#             a += 1
#             b -= 1

#         # Move everything up

#         comp = []
#         print(f"Calculating: {temp[a]} - {temp[b]}")
#         comp.append(abs(temp[a] - temp[b]))

#         start_pointer += 1
#         end_pointer += start_pointer + scan_length - 1
        


    



# print("Start -----------------------------------------")
# for i in range(1, length+1):
#     temp = pic[i:pic[i]-1]
#     print(temp)

#     if len(temp) % 2 == 0:
#         print("length is pair")
#         times = len(temp) // 2
#     else:
#         print("length is odd")
#         times = (len(temp) // 2) + 1
    
#     for j in range(times):
#         print(times)
#         totalSum.append(abs(temp[j] - temp[len(temp) - 1 - j]))
#         print(f"equation: {temp[j]} - {temp[len(temp) - 1 - j]}")
#         print(f"output: {out}")

#     print(f"totalSum: {totalSum} sum: {sum(totalSum)}")
#     out.append(sum(totalSum))
#     print(f"appending to out: {out}")
#     totalSum = []

# print(out)
