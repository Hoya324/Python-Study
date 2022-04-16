from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
result = [0]
sum = 0
for i in range(n):
    sum += arr[i]
    result.append(sum)

for j in range(m):
    s, e = map(int, stdin.readline().split())
    print(result[e] - result[s-1])
