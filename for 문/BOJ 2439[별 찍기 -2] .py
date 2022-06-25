import sys
input = sys.stdin.readline
N = int(input())
for i in range(1,N+1):
    j = N-i
    print(" "*j + '*'*i)
