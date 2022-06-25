not_selfnum_list = []
for i in range(1,10000):
    string = str(i)
    A = list(string)
    result = i + sum(map(int, A))
    not_selfnum_list.append(result)

for i in range(1, 10001):
    if i not in not_selfnum_list:
        print(i)
