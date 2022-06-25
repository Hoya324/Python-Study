import sys

N, M = map(int, sys.stdin.readline().split())

arr = []

for i in range(1, N + 1):
    if N % i == 0 and M % i == 0:
        arr.append(i)

print(max(arr))
print(N * M // max(arr))
