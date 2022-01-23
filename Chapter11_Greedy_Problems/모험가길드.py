from math import floor

n = int(input())

array = list(map(int, input().split()))

total = 0
for i in array:
    total += 1/i

print(floor(total))




