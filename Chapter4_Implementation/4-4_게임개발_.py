n, m = map(int,input().split())
v = [[0] * n for _ in range(m)]

x, y, direction = map(int,input().split())
v[x][y] = 1

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if graph[nx][ny] == 0 and v[nx][ny] == 0:
        v[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        turn_left()
        nx = x - dx[direction]
        ny = y - dy[direction]
        if graph[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)


