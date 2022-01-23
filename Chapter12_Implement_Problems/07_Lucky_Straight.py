data = input()
middle = len(data)//2

left = data[:middle]
right = data[middle:]
left_total=0
right_total=0
for i in range(len(left)):
    left_total += int(left[i])
    right_total += int(right[i])

if left_total == right_total:
    print("LUCKY")
else:
    print("READY")

