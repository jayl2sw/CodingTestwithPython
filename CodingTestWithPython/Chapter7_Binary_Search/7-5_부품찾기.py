def binary_search(array, target, start, end):
    while start<= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

n = int(input())
shop = list(map(int, input().split()))

m = int(input())
order = list(map(int, input().split()))

for item in order:
    if binary_search(shop, item, 0, n-1) is not None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
