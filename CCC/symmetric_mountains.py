# https://cccgrader.com/getproblem.php?fid=928098&authcode=80934a4107f558d515981948eb06ba38
# 1 2 3 4 5 6 7 8 9

length = int(input())
mountains = [int(x) for x in input().split()]

totalSum = []
out = []
count = 0
pointer_A = 0
pointer_B = 0


for scan_length in range(1, length+1):
    for groups in 
    temp = mountains[pointer_A:pointer_A+scan_length-1]

    



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
