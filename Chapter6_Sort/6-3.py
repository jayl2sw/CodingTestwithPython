# 삽입 정렬

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):                              # 처음부터 끝까지
    for j in range(i, 0, -1):                               # j 는 i 부터 0까지 역순으로
        if array[j] < array[j-1]:                           # 만약 j번째가 j-1번째보다 작다면,
            array[j], array[j-1] = array[j-1], array[j]     # 두개 순서를 바꿉니다.
        else:                                               # 그렇게 되면 i번째 전까지 순서대로 바뀜
            break

print(array)