# 7-2.py 재귀 함수로 구현한 이진 탐색 코드
# 데이터가 정렬 되어 있을 때만 효과적으로 사용이 가능하다.
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))


result = binary_search(array, target, 0, n - 1)
if result is None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
