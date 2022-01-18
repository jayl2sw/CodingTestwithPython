n = int(input())
array = list(map(int, input().split()))

d = [0] * 30001

d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(n):
    d[i] = max(d[i-2]+array[i], d[i-1])

print(d[n-1])
