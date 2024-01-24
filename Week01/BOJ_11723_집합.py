import sys

input = sys.stdin.readline

M = int(input())
S = 0

def command(str):
    global S, value
    cmd = str[0]
    if cmd not in ['all', 'empty']:
        value = int(str[1])-1

    if cmd == 'add':
        if S[value] == '0':
            S = S | (1 << value)
            print(S)
    elif cmd == 'remove':
        if value in S:
            S.remove(value)
    elif cmd == 'check':
        if value in S:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if value in S:
            S.remove(value)
        else:
            S.append(value)
    elif cmd == 'all':
        S = [x for x in range(1, 21)]
    elif cmd == 'empty':
        S = []


for _ in range(M):
    cmd = input().split()
    command(cmd)
