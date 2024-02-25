import sys

n, k = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

data.sort(key=lambda x: x[0])  # 나라 번호 순서대로 정렬

result = []
for i in data:  # 한 나라에 대해서
    cnt = 1
    for j in data:  # 나머지 나라 돌면서
        if i[0] == j[0]:  # 같은나라는 비교할 필요 없음
            continue
        if j[1] > i[1]:  # 금메달 수 더 많으면
            cnt += 1  # 등수 하나 늘리고
        elif j[1] == i[1]:  # 금메달 수 같으면
            if j[2] > i[2]:  # 은메달 수 비교
                cnt += 1
            elif j[2] == i[2]:  # 은메달도 같으면
                if j[3] > i[3]:  # 동메달 비교
                    cnt += 1
    result.append(cnt)

print(result[k - 1])
