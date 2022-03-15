def imporved_find_parent(parent, x):
    if parent[x] != x:
        parent[x] = improved_find_parent(parent, parent[x])
    return parent[x]

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


# ==> x를 반환하지 않고 바로 x의 부모 노드 반환함으로써
# x의 루트노드가 바로 부모노드가 된다.
# 시간복잡도 개선
