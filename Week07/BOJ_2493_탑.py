from collections import deque

N = int(input())
top = deque(map(int, input().split()))
tmp = []
ans = [0]*N

for i in range(N - 1, 0, -1):
    if tmp:
        for j in range(len(tmp) - 1, -1, -1):
            if tmp[j][0] <= top[i]:
                ans[tmp[j][1]] = i+1
                tmp.pop()
    tmp.append([top.pop(), i])


print(*ans)