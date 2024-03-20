import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    arr = defaultdict(int)
    # 팀 번호, 팀 점수, 팀의 인원, 팀의 팀의 5번째 선수의 점수.
    team = [[i, 0, 0, 0] for i in range(200)]

    for d in data:
        arr[d] += 1
    score = 1
    for d in data:
        if arr[d] < 6:
            continue
        else:
            team[d-1][1] += score
            team[d-1][2] += 1
            if team[d-1][2] == 5:
                team[d-1][3] = score
        score += 1


