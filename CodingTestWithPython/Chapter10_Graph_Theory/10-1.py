#       그래프           vs     트리
#       방향 or 무방향           방향
#       순환 or 비순환           비순환
#       루트 x                  루트 o
#       상하 x                  상하 o
#       네트워크 모델             계층모델

#   그래프 구현방식   graph(V, E) #(노드, 간선)
#   인접 행렬: 2차원 배열    O(V**2)      모든 노드간의 거리 작성
#   인접 리스트: 리스트 사용  O(E)         노드의 개수만큼 리스트 만들어서 사용


# 서로소 집합
# union(합집합) & find(찾기) 사용

# 10-1 서로소 집합 알고리즘 소스코드

# root 부모를 찾을 때 까지 재귀적으로 호출
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int,input().split())
parent = [0] * (v + 1)

for i in range(1, v+1):
    parent[i] = i

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parent[i], end=' ')


