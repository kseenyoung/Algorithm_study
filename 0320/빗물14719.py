import sys
input=sys.stdin.readline

h,w=map(int,input().split())
block=list(map(int,input().split()))

fi=0
ans=0
h,tmp=0,0
finding=False
for i in range(w):
    if finding:
        if block[i]>=h:
            ans+=tmp
            tmp=0
            finding=False
        else:
            tmp+=h-block[i]
    if i==w-1:
        if tmp>0:
            h,tmp=0,0
            finding=False
            for j in range(i,fi-1,-1):
                if finding:
                    if block[j]>=h:
                        ans+=tmp
                        tmp=0
                        finding=False
                    else:
                        tmp+=h-block[j]
                if block[j-1]<block[j] and not finding:
                    h=block[j]
                    finding=True

    elif block[i+1]<block[i] and not finding:
        fi=i
        h=block[i]
        finding=True
print(ans)