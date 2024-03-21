import sys, heapq as hq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [sys.maxsize]*(N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])  # 양방향 그래프
    graph[b].append([c, a])


q = []
distance[1] = 0  # 현서는 1에서 출발
hq.heappush(q, [0, 1])  # cost 를 먼저 넣어서 낮은 것부터 앞으로 오게 함

while q:
    now_cost, now_node = hq.heappop(q)
    if now_cost > distance[now_node]:  # 현재 노드의 코스트가 이미 저장된 코스트보다 크다면 건너뜀
        continue

    for next_cost, next_node in graph[now_node]:  # 현제 노드에서 갈 수 있는 것 찾음.
        if next_cost + distance[now_node] < distance[next_node]:  #  다음으로 갈 수 있는 노드까지의 코스트보다 작다면
            hq.heappush(q, [next_cost + distance[now_node] , next_node])  # q 와 distance 를 업데이트함
            distance[next_node] = next_cost + distance[now_node]

print(distance[N])