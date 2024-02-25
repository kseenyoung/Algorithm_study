import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
belt = deque(map(int, sys.stdin.readline().split()))
robot = deque([0] * n)

result = 0
while True:
    result += 1  # 단계 추가
    belt.rotate(1)  # 벨트 회전
    robot[-1] = 0  # 맨 끝 로봇 내림
    robot.rotate(1)  # 로봇 회전
    robot[-1] = 0  # 맨 끝 로봇 내림
    for i in range(n - 2, -1, -1):  # 가장 먼저 벨트에 올라간 로봇부터
        if robot[i + 1] == 0 and belt[i + 1] >= 1 and robot[i] == 1:
            # 다음칸에 로봇 없고 내구도 1이상이고 로봇 있으면
            robot[i + 1] = 1  # 다음칸으로 옮기고
            robot[i] = 0  # 지금칸 없애고
            belt[i + 1] -= 1  # 내구도 감소
    robot[-1] = 0  # 맨 끝 로봇 내림
    if robot[0] != 1 and belt[0] != 0:  # 맨 앞거 로봇 없고 내구도 1 이상이면
        robot[0] = 1  # 로봇 올리고
        belt[0] -= 1  # 내구도 감소

    if belt.count(0) >= k:  # 종료 조건
        break

print(result)
