import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
distance = [1e9]*(N+1)
node = [[] for _ in range(N+1)]

for i in range(M):
    a, b, c = map(int, input().split())
    node[a].append((c, b))
    node[b].append((c, a))

que = []
heapq.heappush(que, (0, 1))
distance[1] = 0

while que:
    v, n = heapq.heappop(que)
    if distance[n] < v:
        continue

    for v2, n2 in node[n]:
        cost = v + v2
        if distance[n2] > cost:
            distance[n2] = cost
            heapq.heappush(que, (cost, n2))

print(distance[N])
