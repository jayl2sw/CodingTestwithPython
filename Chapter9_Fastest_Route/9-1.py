# 9-1 Dijkstra 알고리즘
# 출발 노드 설정
# 최단 거리 테이블 초기화
# 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
# 해당 노드를 거쳐 다른 노드로 가느 ㄴ비용을 계산하여 최단 거리 테이블 갱신
# 위 과정에서 3,4번 반복

# 2가지 방법의 구현
# 방법 1. 구현하기 쉽지만 느리게 동작하는 코드
# 방법 2. 구현하기에 조금 더 까다롭지만 빠르게 동작하는 코드

import sys
input = sys.stdin.readline
INF = int(1e9)

# n: 노드의 개수 m: 간선의 개수
n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]

visited = [False] * (n+1)

distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])




