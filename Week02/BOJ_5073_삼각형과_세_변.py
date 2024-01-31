import sys

input = sys.stdin.readline

while 1:
    a, b, c = tuple(map(int, input().split()))
    if (a, b, c) == (0, 0, 0):
        exit()

    if max(a, b, c) >= sum([a, b, c])-max(a, b, c):
        print("Invalid")
        continue

    if a == b and a == c and b == c:
        print("Equilateral")
    elif ((a == b) and (a != c)) or ((a == c) and (a != b)) or ((b == c) and (a != b)):
        print("Isosceles")
    elif a != b and a != c and b != c:
        print("Scalene")

