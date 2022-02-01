import sys

def Test():
    global C
    for i in range(C):
        N, *S = map(int, sys.stdin.readline().split())
        arr = sum(S)/N
        count = 0
        for j in range(N):
            if S[j] > arr:
                count +=1
        per = count/N*100
        return print("{0:0.3f}".format(per)+"%")

C = int(input())
for i in range(C):
    Test()
