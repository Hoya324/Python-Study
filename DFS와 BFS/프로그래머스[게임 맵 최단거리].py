from collections import deque


def ROR(maps):
    n, m = len(maps), len(maps[0])
    dr = [[0, 1] ,[0, -1], [1, 0], [-1, 0]]

    road = deque()
    road.append([0, 0])

    while road:
        data = road.popleft()
        y = data[0]
        x = data[1]

        for dy, dx in dr:
            ny = y + dy
            nx = x + dx

            if ny >= n or ny < 0 or nx >= m or nx < 0:
                continue

            if maps[ny][nx] == 0:
                continue

            if maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                road.append([ny, nx])


    return maps[n-1][m-1]


def solution(maps):
    answer = ROR(maps)
    if answer == 1:
        return -1
    return answer

