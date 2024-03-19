import sys
input = sys.stdin.readline

N, gameType = input().split()
dic = {}
for i in range(int(N)):
    name = input()
    dic[name] = 1
if gameType == 'Y':
    print(len(dic))
elif gameType == 'F':
    print(len(dic)//2)
elif gameType == 'O':
    print(len(dic)//3)