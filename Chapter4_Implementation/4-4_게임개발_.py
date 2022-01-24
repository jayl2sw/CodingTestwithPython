# n행 m열의 맵 생성
n, m = map(int, input().split())
x, y, direction = map(int,input().split())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

graph =[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

visited = [[0] * m for _ in range(n)]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    turn_left()
    turn_time += 1
    nx = x + dx[direction]
    ny = y + dy[direction]

    if visited[nx][ny] == 0 and graph[nx][ny] == 0:
        visited[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time +=1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if graph[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time =0
print(count)





