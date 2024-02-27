import sys
from collections import deque
input = sys.stdin.readline

N, K = tuple(map(int, input().split()))
belt = deque(map(int, input().split()))
robot = deque([0]*N)
count = belt.count(0)
ans = 0

while count < K:
    ans += 1
    belt.appendleft(belt.pop())  # 벨트 한 칸 회전함.
    robot.pop()
    robot.appendleft(0)  # 로봇도 한 칸 같이 회전.
    if robot[N-1] == 1:  # 로봇이 내리는 위치일 때 즉시 내림
        robot[N-1] = 0

    for i in range(N-2, 0, -1):
        if robot[i] == 1:
            if belt[i+1] >= 1 and robot[i+1] == 0:  # belt 의 내구도가 1 이상이고 로봇이 없을 때.
                if i == N-2:   # 내리는 위치에 로봇을 놓을 수 있을 때.
                    belt[i+1] -= 1
                    if belt[i+1] == 0:  #  벨트의 내구도가 0 이 되면 count + 1
                        count += 1
                    robot[i], robot[i+1] = 0, 0
                else:
                    belt[i+1] -= 1   # 옆으로 한 칸 이동할 때.
                    if belt[i+1] == 0:
                        count += 1
                    robot[i] = 0
                    robot[i+1] = 1

    if belt[0] >= 1:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            count += 1

print(ans)

