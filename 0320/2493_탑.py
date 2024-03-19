import sys

n = int(sys.stdin.readline().strip())
data = list(map(int, sys.stdin.readline().split()))

stack = []
for i in range(n):
    while len(stack) != 0 and stack[-1][0] < data[i]:
        stack.pop()

    if len(stack) == 0:
        print(0, end=' ')
    else:
        print(stack[-1][1], end=' ')
    stack.append([data[i], i + 1])
