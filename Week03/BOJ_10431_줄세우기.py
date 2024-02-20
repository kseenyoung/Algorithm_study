import sys
from collections import deque

input = sys.stdin.readline

P = int(input())

for p in range(1, P + 1):
    case = deque(list(map(int, input().split())))
    case.popleft()
    result = []
    ans = 0
    while case:
        n = case.popleft()
        if not result:
            result.append(n)
        else:
            flag = 0
            for i in range(len(result)):
                if n < result[i]:
                    result.insert(i, n)
                    ans += len(result) - i - 1
                    flag = 1
                    break
            if not flag:
                result.append(n)

    print("{} {}".format(p, ans))
