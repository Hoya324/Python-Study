import sys
n, m, *card = map(int, sys.stdin.read().split())

result = []
#경우의 수는 n*(n-1)*(n-2)
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            Plus = card[i] + card[j] + card[k]
            if Plus <= m:
                result.append(Plus)

print(max(result))
