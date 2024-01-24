import sys, math
input = sys.stdin.readline

H, W, N, M = map(int, input().split())

print(math.ceil(H/(N+1)) * math.ceil(W/(M+1)))
