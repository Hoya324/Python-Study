from sys import stdin

a, b, c = map(int, stdin.readline().split())

def divide(a, b):
    if b == 1:
        return a
    if b % 2 == 0:
        result = divide(a, b/2)
        return result*result
    else:
        result = divide(a, (b-1)/2)
        return result*result*a
    

print(divide(a, b) % c)