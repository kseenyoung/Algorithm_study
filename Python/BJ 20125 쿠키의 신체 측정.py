import sys

input = sys.stdin.readline

N = int(input())
heart = [0, 0]
result = [0 for i in range(5)]
board = [list(map(str, input())) for _ in range(N)]
# print(map)

# 심장 찾기
for i in range(N):
    if heart[0] == 0:
        for j in range(N):
            if board[i][j] == '*':
                heart = [i + 1, j]
                break

# 왼쪽 팔
cnt = 0
for col in range(heart[1]-1, -1, -1):
    if board[heart[0]][col] == '*':
        cnt += 1
    else:
        break
result[0] = cnt
# 오른쪽 팔
cnt = 0
for col in range(heart[1]+1, N):
    if board[heart[0]][col] == '*':
        cnt += 1
    else:
        break
result[1] = cnt

# 허리
cnt = 0
endRow = 0
for row in range(heart[0] + 1, N):
    if board[row][heart[1]] == '*':
        cnt += 1
    else:
        endRow = row
        break
result[2] = cnt
cnt = 0

# 왼 다리
for row in range(endRow, N):
    if board[row][heart[1] - 1] == '*':
        cnt += 1
    else:
        break
result[3] = cnt
cnt = 0

# 오른 다리
for row in range(endRow, N):
    if board[row][heart[1] + 1] == '*':
        cnt += 1
    else:
        break
result[4] = cnt

print(heart[0]+1, heart[1]+1)
print(result[0], result[1], result[2], result[3], result[4])