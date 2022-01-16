# 3-1.py
n = 1260
count = 0

coin_type = [500, 100, 50, 10]


for coin in coin_type:
    times = n // coin
    n -= coin*times
    count += times

print(count)
