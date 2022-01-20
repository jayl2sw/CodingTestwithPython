# 위상 정렬 : 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것.
# 진입 차수 : 특정한 노드로 들어오는 간선의 개수

# 1. 진입 차수가 0인 노드를 큐에 넣는다
# 2. 큐가 빌 때까지 다음 과정을 반복한다.
#   i. queue.pop() 후 해당 노드에서 출발하는 간선 제거
#   ii. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.

from collections import deque

v, e = map(int,input().split())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)

graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort(graph):
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort(graph)