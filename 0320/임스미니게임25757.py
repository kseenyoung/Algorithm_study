import sys
input=sys.stdin.readline
n,cmd=input().split()

s=set()
for _ in range(int(n)):
    s.add(input())

if cmd=='Y':
    print(len(s))
elif cmd=='F':
    print(len(s)//2)
else:
    print(len(s)//3)