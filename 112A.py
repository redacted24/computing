# https://codeforces.com/problemset/problem/112/A4
# Petya and Strings

a = str(input())
b = str(input())

a = a.lower()
b = b.lower()


if a < b:
  print("-1")
elif a == b:
  print("0")
else:
  print("1")
