import sys
input=sys.stdin.readline

N,L,R=map(int,input().split())

world=[ list(map(int,input().split())) for _ in range(N)]
# visited=[ [False]*N for _ in range(N) ]
# checking=True
# while checking:
#     for i in range(N):
#         for j in range(N):
#             if visited[i][j]:
#                 continue
#             bfs(i,j,visited)
#








# union-find
# parent=[]
# popu={}
# for i in range(N):
#     for j in range(N):
#         parent.append(i*N+j)
# def union(a,b):
#     ar,br=find(a),find(b)
#     if ar==br:
#         return False
#     parent[a]=br
#     return True
# def find(x):
#     if parent[x]==x:
#         return x
#     parent[x]=find(parent[x])
#     return parent[x]
#
# checking=True
# while checking:
#     for i in range(N-1):
#         for j in range(N-1):
#             cur=i*N+j
#             if L<=abs(parent[i][j]-parent[i+1][j])<=R:
#                 tmp=cur+N
#                 npop=parent[i][j]
#                 if union(cur,tmp):
#                     popu[br]