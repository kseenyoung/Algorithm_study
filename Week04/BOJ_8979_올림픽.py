import sys
input = sys.stdin.readline

N, K = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

grade = [arr[i][0] for i in range(N)].index(K)   # K 국가의 등수

for i in range(N):
    if arr[i][1:] == arr[grade][1:]:  # 처음 자신이랑 동점인 국가가 나오면 그 등수로, 아니면 자기 자신의 등수 그대로
        print(i+1)
        exit(0)
