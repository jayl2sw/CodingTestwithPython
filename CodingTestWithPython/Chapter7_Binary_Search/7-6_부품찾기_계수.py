n = int(input())
array = [0] * 10001

for item in list(map(int,input().split())):
    array[item] += 1


m = int(input())
for order in list(map(int, input().split())):
    if array[order] > 0:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

