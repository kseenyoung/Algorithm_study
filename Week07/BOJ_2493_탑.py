from collections import deque
import copy
import heapq as hq

N = int(input())
top = deque(map(int, input().split()))
first = copy.deepcopy(top)
tmp = []
ans = [0]*N

for i in range(N - 1, -1, -1):    # 탑의 오른쪽부터 탐색
    if tmp:   #  담아놓은 탑이 있을 때
        for j in range(len(tmp) - 1, -1, -1):
            if tmp[j][0] > -top[i]:    # tmp의 탑을 돌면서 현재의 탑보다 작으면
                ans[tmp[j][1]] = i+1   # 현재 index가 그 탑의 답이 된다
                tmp.pop()
            else:
                break
    hq.heappush(tmp, [-top.pop(), i])   # 내림차순으로 정렬


print(*ans)