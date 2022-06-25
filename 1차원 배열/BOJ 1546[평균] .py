import sys
A = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().split()))
High = max(B) 
print(sum(B)/(High*A)*100)
