import sys
from collections import deque
input = sys.stdin.readline

P = int(input())

for p in range(1, P+1):
    case = deque(list(map(int, input().split())))
    case.popleft()
    result = deque()
    ans = 0
    while 1:
        tmp = ans
        while case:
            n = case.popleft()
            flag = 0
            if result:
                for r in result:
                    if r > n:
                        result.appendleft(n)
                        ans += len(result)-1
                        flag = 1
                        break
            if not flag:
                result.append(n)
        if tmp == ans:
            break

    print("{} {}".format(p, ans))


