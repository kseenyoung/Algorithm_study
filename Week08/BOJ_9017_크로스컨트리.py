import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    arr = defaultdict(int)
    team = [[0, i] for i in range(200)]

    for d in data:
        arr[d] += 1
    score = 1
    for d in data:
        if arr[d] < 6:
            continue
        else:
            team[d-1][0] += score
        score += 1

    print(team)
