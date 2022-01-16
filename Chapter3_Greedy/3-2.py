n, m, k = map(int,input().split())
data = list(map(int, input().split()))

data.sort()
count = 0
total = 0
while True:
    if count == m:
        break
    for i in range(k):
        total += data[-1]
        count += 1
        if count == m:
            break
    total += data[-2]
    count += 1
print(total)

# 더 쉬운 방법
n, m, k = map(int,input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

time_second = m // k
time_first = m - time_second

total = first * time_first + second * time_second
print(total)

