# 7-7 set 사용
n = int(input())
shop = set(map(int, input().split()))

m = int(input())
order = list(map(int,input().split()))

for item in order:
    if item in shop:
        print("yes", end=' ')
    else:
        print("no", end=' ')