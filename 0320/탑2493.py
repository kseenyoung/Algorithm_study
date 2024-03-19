n=int(input())
li=list(map(int,input().split()))

s=[]

for i in range(n-1,0,-1):
    front=li[i-1]
    if li[i]<front:
        li[i]=i
        while s:
            x=s.pop()
            if li[x]<front:
                li[x]=i
            else:
                s.append(x)
                break
    else:
        s.append(i)

for i in s:
    li[i]=0
li[0]=0

print(*li)
