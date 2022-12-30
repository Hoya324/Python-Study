from sys import stdin

arr = []

for i in range(9):
    arr.append(list(map(int, stdin.readline().split())))

max_int = 0
row = 0
col = 0
for i in range(9):
    for j in range(9):
        if max_int < arr[i][j]:
            max_int = arr[i][j]
            row, col = i, j
        
print(max_int)
print(row+1, col+1)
