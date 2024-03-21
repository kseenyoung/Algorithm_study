import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [sys.maxsize for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([cost, b])
    graph[b].append([cost, a])

def dijkstra():
    q = []
    distance[1] = 0 # 현서가 출발하는 위치 1
    heapq.heappush(q, [0, 1])  #  dist, node

    while q:
        print(q)
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:   # next : (node, cost)
            cost = next[1] + distance[node]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, [cost, next[0]])

dijkstra()
print(distance[N])

