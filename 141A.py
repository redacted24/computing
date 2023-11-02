# https://codeforces.com/problemset/problem/141/A
# Amusing Joke

a = list(input())
b = list(input())
a.extend(b)
pile = list(input())
a.sort()
pile.sort()

if a == pile:
    print("YES")
else:
    print("NO")