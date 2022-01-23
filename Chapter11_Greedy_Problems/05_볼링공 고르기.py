n, m = map(int,input().split())
array = list(map(int,input().split()))
d = [0] * (m+1)

for ball in array:
    d[ball] += 1

total = n*(n-1)/2

balls = []
for i in d:
    if i >= 2 :
        total -= i*(i-1)/2


print(int(total))