import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    arr = defaultdict(int)
    # 팀 번호, 팀 점수, 팀의 인원, 팀의 팀의 5번째 선수의 점수.
    team = [[i, 0, 0, 0] for i in range(201)]

    for d in data:
        arr[d] += 1
    score = 1
    for d in data:
        if arr[d] < 6:   # 6인 미만의 팀은 건너뜀.
            continue
        else:
            if team[d][2] <= 3:   # 팀 4명까지 점수를 더해줌
                team[d][1] += score
                team[d][2] += 1
            else:   # 팀의 4명 이상일 경우 인원만 더함.
                team[d][2] += 1
            if team[d][2] == 5:   # 점수가 같을 경우를 위해 5번째 사람의 점수를 저장해줌.
                team[d][3] = score
            score += 1

    team.sort(key=lambda x: [x[1], x[3]])   # 총 점수와 5번째 사람의 점수(중복일 경우를 위해)로 정렬

    for i in range(len(team)-1, -1, -1):  # 뒤에서부터 탐색하여 마지막으로 점수가 존재하는 조가 1등임.
        if team[i][1] == 0:
            print(team[i+1][0])
            break

