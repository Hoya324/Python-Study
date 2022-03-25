T = int(input())
arr = [[] for _ in range(15)]
for i in range(1, 15):
        arr[0].append(i)


for j in range(1, 15):
    for i in range(1, 15):
        data = 0
        for k in range(0, i):
            data += arr[j-1][k]
        arr[j].append(data)

for _ in range(T):
    a = int(input())
    b = int(input())
    print(arr[a][b-1])
