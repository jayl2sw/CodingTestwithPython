n = int(input())
plans = list(input().split())

moves = ["U", "D", "L", "R"]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
x = 1
y = 1
for plan in plans:
    for j in range(len(moves)):
        if plan == moves[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or ny < 1 or nx >= n or ny >= n:
        continue
    else:
        x, y = nx, ny
print(x, y)