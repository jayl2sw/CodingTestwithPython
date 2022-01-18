n, m = map(int,input().split())
data = list(map(int,input().split()))

start = 0
end = max(data)
def binary_search(array, start, end):
    result = 0
    while start <= end:
        total = 0
        mid = (start + end)//2
        for x in array:
            if x > mid:
                total += x - mid
        if total < m:
            end = mid - 1

        else:
            result = mid
            start = mid + 1
    return result

print(binary_search(data, start, end))
