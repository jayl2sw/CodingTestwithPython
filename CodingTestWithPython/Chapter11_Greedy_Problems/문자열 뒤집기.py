from math import ceil

input = list(input())

list = []
for i in range(len(input)-1):
    if input[i] != input[i+1]:
        list.append("1")
    else:
        list.append("0")

result = 0
for digit in list:
    result += int(digit)

if result % 2 == 0:
    print(result // 2)
else: print(ceil(result /2))