from sys import stdin

N = int(stdin.readline())

arr = []
for i in range(N):
    a = list(map(int, stdin.readline().split()))
    arr.append(a)

# 두번째 값으로 먼저 우선순위를 정하고 같을 경우 첫번째 값으로 비교한다.
arr.sort(key = lambda x : (x[1], x[0]))

for i in range(N):
    print(arr[i][0], arr[i][1])
