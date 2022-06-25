from sys import stdin

K, N = map(int, stdin.readline().split())
lan = list(map(int, stdin.read().split()))


start, end = 1, max(lan)
while start <= end:
    mid = (start + end) // 2
    lines = 0

    for i in lan:
        lines += i // mid

    # 나눠지는 랜선의 양이 목표값보다 더 많으면 탐색 시작점을 중간보다 한 칸 앞으로,
    # 나눠지는 랜선의 양이 목표값보다 더 적으면 탐색 끝점을 중간보다 한 칸 뒤로,
    # 위 과정을 반복하면서 start > end 인 상황이 오면 start는 이미 범위 밖이므로 end 출력
        
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1
    
print(end)
