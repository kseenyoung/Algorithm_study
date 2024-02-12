import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()


def ab(string):
    if string == s:  # 만들수 있음
        print(1)
        exit(0)
    if len(string) == 0:  # 다 왔는데도 못만듦
        return
    if string[-1] == 'A':  # 맨 뒤가 a라면
        ab(string[:-1])  # 맨 뒤 빼줌
    if string[0] == 'B':  # 맨 앞이 b라면
        ab(string[1:][::-1])  # 맨 앞 빼고 뒤집음


ab(t)
print(0)
