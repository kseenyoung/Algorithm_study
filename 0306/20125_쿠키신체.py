import sys

n = int(sys.stdin.readline())

data = [list(sys.stdin.readline().strip()) for _ in range(n)]

x, y = -1, -1

for i in range(n): 
  for j in range(n):
    if data[i][j] == '*' and x == -1 and y == -1:
      x, y = i+1, j
      break

result = []

# 팔 길이
left, right = 0, 0
for i in range(n):
  if data[x][i] == "*":
    if i < y:
      left += 1
    elif i > y:
      right += 1
  if left != 0 and right != 0 and data[x][i] == "_":
    break
result += [left, right]
    
# 허리 길이
mid = 0
for i in range(x+1, n):
  if data[i][y] == "*":
    mid += 1
  else:
    break
result.append(mid)

# 다리 길이
left, right = 0, 0
for i in range(x+mid, n):
  if data[i][y-1] == "*":
    left += 1
  if data[i][y+1] == "*":
    right += 1
  if left != 0 and right != 0 and data[i][y+1] == "_" and data[i][y-1] == "_":
    break
result += [left, right]

print(x+1, y+1)
print(*result)
