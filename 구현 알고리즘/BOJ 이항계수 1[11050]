from sys import stdin

N, R = map(int, stdin.readline().split())
result = 1
if (R < N/2+1):
    for i in range(1, R + 1):
        result *= N
        result //= i
        N -= 1
else:
    R = N - R
    for i in range(1, R + 1):
        result *= N
        result //= i
        N -= 1
        
print(result)
