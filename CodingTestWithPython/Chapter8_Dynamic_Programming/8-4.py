# Bottom up - 다이나믹 프로그래밍의 전형적인 형태
# 메모제이션 -> 탑다운 방식
d = [0] * 100 # DP 테이블

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])