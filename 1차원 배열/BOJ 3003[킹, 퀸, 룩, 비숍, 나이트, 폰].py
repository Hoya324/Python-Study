import sys

sample = [1, 1, 2, 2, 2, 8]
data = list(map(int, sys.stdin.readline().split()))
for i in range(6):
    print(sample[i] - data[i])