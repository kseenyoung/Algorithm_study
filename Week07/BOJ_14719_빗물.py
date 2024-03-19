import sys

input = sys.stdin.readline

H, W = map(int, input().split())
block = list(map(int, input().split()))
ans = 0

arr = [[0] * W for _ in range(H)]

for i in range(len(block)):
    now = block[i]
    for j in range(now):
        arr[j][i] = 1

for i in range(H):
    if arr[i][0] == 0:   # 0번째에 벽이 없을 때, 중간에 만나는 벽이 시작이 되도록 해줬음
        start = -1
    else:
        start = 0
    count = 0
    for j in range(W):
        if arr[i][j] and count == 0:
            start = j
        elif arr[i][j] and count > 0 and start >= 0:
            ans += count
            count = 0
            start = j
        elif arr[i][j] == 0 and start >= 0:
            count += 1

print(ans)
