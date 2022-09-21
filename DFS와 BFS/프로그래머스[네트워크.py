def solution(n, computers):
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            visited = network(i, computers, visited, n)
            count += 1
    
    return count



def network(location, computers, visited, n):
    visited[location] = True
    for i in range(n):
        if not visited[i] and location != i and computers[location][i] == 1:
            network(i, computers, visited, n)

    return visited
