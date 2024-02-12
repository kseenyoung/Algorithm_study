import sys

n = int(sys.stdin.readline().strip())

cnt = 0

if n == 1:
    print(1)
else:
    n -= 1  # 맨 처음 위치
    while n > 0:  # 번호 남아있을 동안
        cnt += 1  # 한줄 가고
        n = n - 6 * cnt  # 그 한바퀴 다 빼줌
    print(cnt + 1)
