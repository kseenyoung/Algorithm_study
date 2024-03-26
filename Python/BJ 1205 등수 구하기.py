import sys
input = sys.stdin.readline

N, new, P = map(int, input().split())

if N == 0:
    print(1)
else:
    scores = [int(i) for i in input().split()]
    scores.append(new)
    scores.sort(reverse=True)

    idx = scores.index(new) + 1  # 등수
    if idx > P:
        print(-1)
    elif N == P and new == scores[-1]:
        print(-1)
    else:
        print(idx)
