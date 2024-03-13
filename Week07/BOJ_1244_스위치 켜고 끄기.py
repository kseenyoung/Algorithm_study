import sys

input = sys.stdin.readline

""" 
남학생:1 여학생:2
남학생의 경우, 자기가 받은 수의 배수의 스위치를 토글.
여학생의 경우, 받은 수를 중심으로 좌우가 대칭인 스위치를 가장 많이 포함하는 구간을 찾아 그 구간의 스위치 상태를 모두 바꿈.
"""


def male(x):
    tmp = x
    while 1:
        if tmp >= N:
            return
        switch[tmp - 1] = abs(switch[tmp - 1] - 1)
        tmp += x


def female(x):
    limit = min(x, N - x)
    switch[limit - 1] = abs(switch[limit - 1] - 1)
    for i in range(1, limit):
        if switch[limit - i - 1] != switch[limit + i - 1]:  # 스위치의 상태가 같지 않다면
            break
        else:
            switch[limit - i - 1] = abs(switch[limit - i - 1] - 1)
            switch[limit + i - 1] = abs(switch[limit + i - 1] - 1)
    return


N = int(input())  # 스위치 개수
switch = list(map(int, input().split()))
S = int(input())  # 학생 수
student = [list(map(int, input().split())) for _ in range(S)]
for gender, num in student:
    if gender == 1:
        male(num)
    else:
        female(num)

if N > 20:
    i = 0
    while 1:
        if i+20 >= N:
            break
        print(*switch[i:i+20])
    print(*switch[i:])
else:
    print(*switch)