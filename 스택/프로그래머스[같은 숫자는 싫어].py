def solution(arr):
    answer = []
    for i in range(len(arr)):
        if i != len(arr)-1 and arr[i] != arr[i+1]:
            answer.append(arr[i])
        elif i == len(arr)-1:
            answer.append(arr[i])
    return answer