import sys

while True:
    data = list(map(int, sys.stdin.readline().split()))
    data.sort()
    a, b, c = data
    if a == 0 and b == 0 and c == 0:
        break
    if c >= a + b:
        print("Invalid")
    elif a == b and b == c and c == a:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")
