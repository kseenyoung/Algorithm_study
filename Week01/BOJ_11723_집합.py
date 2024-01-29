import sys
input = sys.stdin.readline

M = int(input())
S = 0b0


def command(str):
    global S, x
    cmd = str[0]
    if cmd not in ['all', 'empty']:   # x 가 존재 할 때
        x = int(str[1])-1

    if cmd == 'add':   # x 를 더하는 연산일 때,
        S = S | (0b1 << x)  # 1이 하나만 있으면 1이되는 or 연산을 통해 있게 함

    elif cmd == 'remove':  # x 를 빼는 연산일 때,
        S = S & ~(0b1 << x)   # x 가 있든 없든 (1, 0) 아니면 (0, 0) 이므로 and ! 연산으로 빼줌

    elif cmd == 'check':
        if S & (0b1 << x):  # 둘 다 1이어야 하므로
            print(1)
        else:
            print(0)

    elif cmd == 'toggle':
        S = S ^ (0b1 << x)   # xor 연산을 통해 없으면(!=) 더하고, 있으면 (=) 뺌. (다르면 1, 같으면 0 이 되는 xor 을 이용)

    elif cmd == 'all':
        S = 0b11111111111111111111

    elif cmd == 'empty':
        S = 0b0


for _ in range(M):
    cmd = input().split()
    command(cmd)
