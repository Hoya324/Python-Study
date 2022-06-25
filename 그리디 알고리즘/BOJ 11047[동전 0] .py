#동전 종류 N, 총 K원
import sys
N, K = map(int, sys.stdin.readline().split())
values_list = []
for _ in range(N):
    values = int(input())
    values_list.append(values)
values_list.reverse()
count = 0
for i in values_list:
    if K >= i:
        count += K//i
    K %= i
print(count)
