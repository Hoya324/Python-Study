def solve(T):
    UP = T.upper()
    num = {}
    for i in UP:
        if i in num.keys():
            num[i] += 1
        else:
            num[i] = 1
        big = max(num.values())
    count = 0
    for key in num.keys():
        if num[key] == big:
            count += 1
            result = key
    if count > 1:
        print('?')
    else:
        print(result)
T = input()
solve(T)
