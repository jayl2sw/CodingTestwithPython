# 신장트리: 하나의 그래프가 있을 때, 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
# ==> 트리의 성립 조건

# 최소 비용으로 신장 트리를 찾아야 할 때, 크루스칼 알고리즘 사용
# 1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
#       i. 사이클이 발생하지 않는 경우 최소 신장트리에 포함
#       ii. 사이클이 발생하는 경우 포함 x
# 3. 모든 간선에 대하여 2번의 과정을 반복한다.

def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0

for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보 입력받기
for _ in range(e):
    a, b, cost = map(int,input().split())
    edges.append((cost, a, b))


# 간선을 비용 순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent, b):
        union_parent(parent,a, b)
        result += cost

print(result)


