import sys
import math

input = sys.stdin.readline
N = int(input())
M = int(input())

primenumber_list = []

def primenumber(i):
  for j in range(2, int(math.sqrt(i)) + 1):
    if i % j == 0:
      return 0
  return 1

for i in range(N, M+1): 
  if i == 1:
    continue
  if primenumber(i) == 1:
    primenumber_list.append(i)


if len(primenumber_list) == 0:
  print(-1)
else:  
  print(sum(primenumber_list))
  print(min(primenumber_list))
