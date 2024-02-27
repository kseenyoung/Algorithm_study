import sys
from collections import deque
input = sys.stdin.readline

N, K = tuple(map(int, input().split()))
belt = deque(map(int, input().split()))
robot = deque([0]*N)
count = 0
print(robot)
# 초기 상태
robot[0] = 1  # 로봇이 올리는 위치에 올라가고
belt[0] -= 1  # 1번째 위치의 내구도는 하나 내려감.
if not belt[0]:  # 만약 0 이 되었다면 count 1 올려줌.
    count += 1

while count < K:
    belt.appendleft(belt.pop()) # 벨트 한 칸 회전함.
    robot.pop()
    robot.appendleft(0) # 로봇도 한 칸 같이 회전.

    for i in range(N-2, -1, -1):
        if belt[i+1] and not robot[i+1]:
            if i == N-2:
                belt[i+1] -= 1
                robot[i]
