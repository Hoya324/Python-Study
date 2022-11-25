list = [0 for i in range(5)]
total = 0
for i in range(5):
    list[i] = int(input())
    total += list[i]

print(total//5)
list.sort()
print(list[2])
