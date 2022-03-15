input_data = input()
english = []
number = ['0','1','2','3','4','5','6','7','8','9']
numbers = 0
for i in input_data:
    if i in number:
        numbers += int(i)
    else:
        english.append(i)

english.sort()
english.append(str(numbers))

result = ''
for char in english:
    result = result + char



print(result)
