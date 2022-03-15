n, m = map(int, input().split())
# n = types 개수
# m = 총 돈양

types = []
for i in range(n):
    types.append(int(input()))

d = [10001] * (m+1)

for i in range(m+1):
    for money in types:
        if i % money == 0:
            d[i] = min(d[i], i // money)
        if i > money:
            d[i] = min(d[i], d[i-money]+1)

if d[m] != 10001:
    print(d[m])
else:
    print("-1")





