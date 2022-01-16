# 재귀함수 왜안됨?


def recursive_function(i):
    if i == 100:
        return
    print(i)
    recursive_function(i+1)
    print(i)

recursive_function(1)
