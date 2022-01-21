from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1, 0, 1, 0]
dy = [0, -1, -0, 1]

print(graph)

def bfs(x, y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        print(x,y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or ny < 0 or nx >= n or ny >= m:
              continue

            if graph[nx][ny] == 1:
               graph[nx][ny] = graph[x][y] + 1
               q.append((nx, ny))

    for i in graph:
        print(i)
    return graph[n-1][m-1]





print(bfs(0,0))









