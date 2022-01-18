# Dynamic Programming의 2가지 방식
# Top-down
# Bottom-up

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(4))