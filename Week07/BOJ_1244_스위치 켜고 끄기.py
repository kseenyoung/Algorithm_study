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
        if tmp-1 >= N:
            return
        switch[tmp - 1] = abs(switch[tmp - 1] - 1)
        tmp += x

def female(x):
    switch[x-1] = abs(switch[x-1]-1)
    i = 1
    while 1:
        if not (0 <= x-i-1 < N) or not (0 <= x+i-1 < N):
            return
        else:
            if switch[x-i-1] == switch[x+i-1]:
                switch[x - i - 1] = abs(switch[x - i - 1] - 1)
                switch[x + i - 1] = abs(switch[x + i - 1] - 1)
            else:
                return
        i += 1

N = int(input())  # 스위치 개수
switch = list(map(int, input().split()))
S = int(input())  # 학생 수
student = [list(map(int, input().split())) for _ in range(S)]
for gender, num in student:
    if gender == 1:
        male(num)
    else:
        female(num)

i = 0
while i < N:
    print(*switch[i:i+20])
    i += 20


