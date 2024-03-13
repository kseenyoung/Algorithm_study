import sys

input = sys.stdin.readline


def game(G):
    if G == 'Y':
        return 1
    if G == 'F':
        return 2
    return 3


N, G = input().split()
name = {input() for _ in range(int(N))}
print(len(name)//game(G))
