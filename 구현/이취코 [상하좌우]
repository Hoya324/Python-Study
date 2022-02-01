#여행가A가 N X N 크기의 정사각형 공간 위에 있다.
#출발점이 (1, 1)이며, 가장 오른 쪽 아래의 좌표는 (N, N)이다.
#여행가 A가 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
#계획서가 주어질 때 A가 최종적으로 도착할 좌표를 출력해라


#N값 입력
import sys
N = int(input())
plans = list(map(str, sys.stdin.readline().split()))
x, y = 1, 1

#L, R, U, D에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
map_type = ['L', 'R', 'U', 'D']

#이동계획 확인
for plan in plans:
    nx = x + dx[map_type.index(plan)]
    ny = y + dy[map_type.index(plan)]
    #print(nx, ny)
    #공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue
    x, y = nx, ny
print(x, y)
