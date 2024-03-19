import sys

n, kind = sys.stdin.readline().split()
n = int(n)

name = {sys.stdin.readline().strip() for _ in range(n)}

if kind == "Y":
    print(len(name))
elif kind == "F":
    print(len(name) // 2)
elif kind == "O":
    print(len(name) // 3)
