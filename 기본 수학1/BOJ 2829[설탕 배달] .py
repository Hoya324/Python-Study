import sys
input = lambda: sys.stdin.readline()

def solution(N):
    result = []
    for a in range(N//5+1):       
        if 5*a+3*((N - a*5)//3) == N:
            result.append(a+(N - a*5)//3)
    if len(result) == 0:
        return -1
    return min(result)
    
        
        

N = int(input())
S = solution(N)
print(S)
