import sys
input=sys.stdin.readline

N=int(input())
switch=list(map(int,input().split()))

for _ in range(int(input())):
    s, i=map(int,input().split())
    if s==1:
        for k in range(i-1,N,i):
            switch[k]=1-switch[k]
    else:
        lim=min(i-1,N-i)
        i-=1
        switch[i]=1-switch[i]
        for k in range(1,lim+1):
            if switch[i+k]!=switch[i-k]:
                break
            switch[i+k]=1-switch[i+k]
            switch[i-k]=switch[i+k]
for i in range(0,N,20):
    print(*switch[i:i+20])