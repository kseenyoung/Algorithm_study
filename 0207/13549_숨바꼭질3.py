import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

data = [-1 for _ in range(100002)]


def bfs(start, end):
    data[start] = 0
    queue = deque([start])
    while queue:
        u = queue.popleft()
        if u == end:
            return data[u]
        if 0 <= 2 * u < 100001 and data[2 * u] == -1:
            data[2 * u] = data[u]
            queue.append(2 * u)
        if 0 <= u - 1 < 100001 and data[u - 1] == -1:
            data[u - 1] = data[u] + 1
            queue.append(u - 1)
        if 0 <= u + 1 < 100001 and data[u + 1] == -1:
            data[u + 1] = data[u] + 1
            queue.append(u + 1)


print(bfs(n, k))
