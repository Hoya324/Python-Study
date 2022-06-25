def Fibonacci_number(N):
    if N <2:
        return N 
    return Fibonacci_number(N-1) + Fibonacci_number(N-2)

N = int(input())
print(Fibonacci_number(N))
