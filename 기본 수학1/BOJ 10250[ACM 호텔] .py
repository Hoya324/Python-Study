#아래층부터 1호라인 다음 2호라인...
import sys
T = int(input())
HWN_list = []
for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    Y = N % H
    X = N // H + 1
    if Y == 0:
        Y = H
        X -= 1
        print(Y*100 + X)
    else:
        print(Y*100 + X)
