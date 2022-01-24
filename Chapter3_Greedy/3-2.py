n, m, k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[-1]
second = data[-2]

total_second = m//(k+1) * second
total_first= (m-(m//(k+1))) * first
total = total_first + total_second

print(total)
# 더 쉬운 방법
# n, m, k = map(int,input().split())
# data = list(map(int, input().split()))
#
# data.sort()
# first = data[-1]
# second = data[-2]
#
# time_second = m // k
# time_first = m - time_second
#
# total = first * time_first + second * time_second
# print(total)

