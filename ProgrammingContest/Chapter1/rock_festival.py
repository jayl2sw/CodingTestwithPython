C = int(input())
for tc in range(1, C+1):
    N, L = map(int, input().split())
    price = list(map(int, input().split()))

    min_value = int(1e9)
    for i in range(L, N):
        for j in range(N - i + 1):
            temp = sum(price[j:j+i])/len(price[j:j+i])
            if min_value > temp:
                min_value = temp

    print(min_value)




