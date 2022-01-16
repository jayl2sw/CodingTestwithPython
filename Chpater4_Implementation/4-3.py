input_data = input()
x = int(input_data[1])
y = int(ord(input_data[0]) - ord("a") + 1)

dx = [2, 2, 1, 1, -2, -2, -1, -1]
dy = [1, -1, 2, -2, 1, -1, 2 ,-2]

count = 0

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > 7 or ny > 7:
        continue
    else:
        count += 1

print(count)