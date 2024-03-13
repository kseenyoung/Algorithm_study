import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())  # L <= (인구 차이) <= R 일 시 국경이 열린다.
area = [list(map(int, input().split())) for _ in range(N)]


def isEdge(x, y):
    if not (0 <= x < N) or not (0 <= y < N):
        return True
    return False


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = 0

while 1:
    visited = [[0] * N for _ in range(N)]
    union = []
    unionPopulation = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                q = deque()
                q.append([i, j])
                tmp = [[i, j]]
                population = area[i][j]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if not isEdge(nx, ny) and not visited[nx][ny]:
                            if L <= abs(area[nx][ny] - area[x][y]) <= R:
                                population += area[nx][ny]
                                q.append([nx, ny])
                                visited[nx][ny] = 1
                                tmp.append([nx, ny])
                if len(tmp) > 1:
                    union.append(tmp)
                    unionPopulation.append(population // len(tmp))
    if not union:
        break
    for i in range(len(union)):
        u = union[i]
        for ux, uy in u:
            area[ux][uy] = unionPopulation[i]
    answer += 1

print(answer)
