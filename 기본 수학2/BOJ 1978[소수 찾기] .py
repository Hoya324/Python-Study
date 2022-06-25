import sys
import math

N = int(input())
M = list(map(int, sys.stdin.readline().split()))
count = 0

def primenumber(M):
  for i in range(2, int(math.sqrt(M)) + 1):
    if M % i == 0:
      return 0
  return 1

for i in range(N): 
  count += primenumber(M[i])
  if M[i] == 1 and count > 0:
    count -= 1
print(count)
