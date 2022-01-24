n, m = map(int,input().split())

for i in range(n):
    data = list(map(int,input().split()))
    max = -999
    if max < min(data):
        max = min(data)

print(max)