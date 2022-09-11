import sys

total = int(input())
N = int(input())
result = 0
for i in range(N):
    a, b = list(map(int, sys.stdin.readline().split()))
    result += a*b

if total == result:
    print("Yes")
else:
    print("No")