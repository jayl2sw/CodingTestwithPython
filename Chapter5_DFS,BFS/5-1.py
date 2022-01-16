# stack 예제

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
print(stack.pop())              # .pop() = stack의 가장 위에 있는 원소를 반환하고 빼냄

print(stack)
print(stack[::-1])