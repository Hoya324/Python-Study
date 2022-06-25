import sys
input = sys.stdin.readline
N = int(input())
for i in range(1,N+1):
    A, B = map(int, input().split())
    plus = A+B
    print('Case #{0}: {1} + {2} = {3}'.format(i,A,B,plus))
