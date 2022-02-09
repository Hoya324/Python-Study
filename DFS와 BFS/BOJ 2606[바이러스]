def dfs_virus(graph, v, visited, Array):
  visited[v] = True
  Array.append(v)
  for i in graph[v]:
    if not visited[i]:
      dfs_virus(graph, i, visited, Array)


import sys
input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for i in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, N + 1):
  graph[i].sort()
  
visited = [False] * (N + 1)
print(visited)
Array = [] 
dfs_virus(graph, 1, visited, Array)
print(len(Array) - 1)
