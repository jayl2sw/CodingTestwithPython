n, m = map(int,input().split())

data1 = list(map(int,input().split()))
data2 = list(map(int,input().split()))

data1.sort()
data2.sort(reverse=True)

for i in range(m):
    if data1[i] < data2[i]:
        data1[i], data2[i] = data2[i], data1[i]
    else:
        break

print(sum(data1))
