# 외벽의 총 둘레
n = int(input())

array = [1,3,4,9,10]
dist = [1,2,3,4]
differences = []

for i in range(len(array)-1):
    difference = array[i+1] - array[i]
    differences.append(difference)

differences.append(array[0] + n - array[-1])

print(differences)