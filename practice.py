from sys import stdin

test = list(input())
a = ""

for i in range(len(test)-1, -1, -1):
    a += str(test[i])

print(a)