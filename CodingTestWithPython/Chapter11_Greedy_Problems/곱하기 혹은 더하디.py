input = input()
expression = ''
for char in input:
    if int(char) == 0:
        expression = expression + char + '+'
    else:
        expression = expression + char + '*'

print(eval(expression[0:-1]))


