List = [int(x) for x in input().split()]
result = []
for i in List:
    _list = list(str(i))
    _list.reverse()
    result.append("".join(_list))
interger = map(int, result)
print(max(interger))
