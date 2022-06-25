# Counter

from sys import stdin
from collections import Counter


N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
data = list(map(int, stdin.readline().split()))

count = Counter(arr)

for i in range(M):
    print(count[data[i]], end = ' ')
    
    
# Hashmap
 
from sys import stdin


N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
M = int(stdin.readline())
data = list(map(int, stdin.readline().split()))

counter = {}

for n in arr:
    if n in counter:
        counter[n] += 1
    else:
        counter[n] = 1

print(' '.join(str(counter[m]) if m in counter else '0' for m in data))
