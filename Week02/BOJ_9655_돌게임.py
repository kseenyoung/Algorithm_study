import sys
input = sys.stdin.readline

N = int(input())
start = 0  # 홀수면 상근, 짝수면 창영이 승리

while N > 0:
    start += 1
    if N >= 3:
        N -= 3
        continue

    if N >= 1:
        N -= 1
        continue

print("CY" if start%2 == 0 else "SK")