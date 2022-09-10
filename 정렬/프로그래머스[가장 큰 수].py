def solution(numbers):
    numbers = list(map(str, numbers))
    numbers_sorted = sorted(numbers, key= lambda x : x*3, reverse=True)
    answer = str(int(''.join(numbers_sorted)))
    return answer

print(solution([3, 30, 34, 5, 9]))