from string import ascii_lowercase

def solve(S):
    List = list(S)
    result = []
    for i in ascii_lowercase:
        if i in List:
            result.append(List.index(i))
        else:
            result.append(-1)
    for i in range(len(result)):
        print(result[i], end = ' ')

S = input()
solve(S)
