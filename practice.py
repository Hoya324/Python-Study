from sys import stdin

n, m = map(int, stdin.readline().split())

a = []
for i in range(n):
    a.append(list(map(int, stdin.readline().split())))

b = []
for i in range(n):
    b.append(list(map(int, stdin.readline().split())))

for i in range(n):
    for j in range(m):
        print(a[i][j] + b[i][j], end=" ")
    print()