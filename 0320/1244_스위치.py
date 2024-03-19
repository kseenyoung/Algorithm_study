import sys

n = int(sys.stdin.readline().strip())
data = [-1] + list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        tmp = 0
        while tmp <= n:
            if data[tmp] == 0:
                data[tmp] = 1
            else:
                data[tmp] = 0
            tmp += b
    elif a == 2:
        if data[b] == 0:
            data[b] = 1
        else:
            data[b] = 0
        for i in range(1, n):
            if b - i > 0 and b + i <= n:
                if data[b - i] == data[b + i]:
                    if data[b - i] == 1:
                        data[b - i] = 0
                    else:
                        data[b - i] = 1
                    if data[b + i] == 1:
                        data[b + i] = 0
                    else:
                        data[b + i] = 1
                else:
                    break
            else:
                break

for _ in range(1, n + 1):
    print(data[_], end=' ')
    if _ % 20 == 0:
        print()
