from collections import deque
import sys

input = sys.stdin.readline

x, K = tuple(map(int, input().split()))
visited = [-1] * 100001
visited[x] = 0
q = deque()
q.append(x)

while q:
    x = q.popleft()
    if x == K:
        break
    for nx in [x - 1, x + 1, x * 2]:
        if not (0 <= nx <= 100000):
            continue
        if visited[nx] == -1:  # 처음 방문하는 경우가 최단거리
            if nx == x * 2:
                visited[nx] = visited[x]
                q.appendleft(nx)
            else:
                visited[nx] = visited[x] + 1
                q.append(x)

print(visited[K])
