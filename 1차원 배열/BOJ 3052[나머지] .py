remainder = []
for i in range(10):
    A = int(input())
    remainder.append(A % 42)
result_set = set(remainder)
print(len(result_set))
