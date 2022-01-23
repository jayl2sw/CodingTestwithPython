from collections import deque

# 의 길이
n = int(input())
# 사과의 개수
k = int(input())

apple_location = []
for i in range(k):
    apple_location.append(list(map(int, input().split())))

# 뱀의 방향 전환 횟수
L = int(input())

time = 0

# L 은 왼쪽 D 는 오른쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

moves = deque()

for i in range(L):
    input_data = input().split()
    moves.append([int(input_data[0]), input_data[1]])


direction = 1


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


def turn_right():
    global direction
    direction += 1
    if direction == 4:
        direction = 0


snake = deque()
x = 1
y = 1
length = n

move = moves.popleft()

while True:
    if x < 1 or y < 1 or x > n or y > n:
        break
    if [x, y] in snake:
        break

    nx = x + dx[direction]
    ny = y + dy[direction]

    snake.append([nx, ny])

    if [nx, ny] in apple_location:
        time += 1
        x = nx
        y = ny
        continue
    else:
        time += 1
        x = nx
        y = ny
        snake.popleft()

    if time == move[0]:
        if move[1] == "D":
            turn_right()
            try:
                move = moves.popleft()
            except:
                continue
        else:
            turn_left()
            try:
                move = moves.popleft()
            except:
                continue


print(time )
