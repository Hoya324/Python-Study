#DFS 정의
def dfs(graph, start, visited_dfs):
    visited_dfs[start] = True
    print(start, end = ' ')
    for i in graph[start]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)

#BFS 정의
from collections import deque

def bfs(graph, start, visited_bfs):
    queue = deque([start])
    visited_bfs[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

#노드의 수 n, 간선의 수 m, 탐색을 시작할 노드 번호 v
import sys
n, m, start = map(int, sys.stdin.readline().split())

#해당하는 graph 정의
graph = [[] for _ in range(n+1)]

#각 노드와 연결되있는 다른 노드를 정의하고 이를 작은 번호순으로 정렬
for _ in range(m):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()

#DFS와 BFS에 각각 graph 부여
graph_dfs = graph
graph_bfs = graph

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

#실행
dfs(graph_dfs, start, visited_dfs)
print()
bfs(graph_bfs, start, visited_bfs)
