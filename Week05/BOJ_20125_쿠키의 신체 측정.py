"""
심장은 처음 나오는 머리의 바로 아래칸 (x+1)
팔은 심장 양 옆으로 
다리는 심장에서 x+1하다가 0됐을때 x+1, y+1 
"""

N = int(input())
cookie = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(N):
        # 머리 등장
        if cookie[i][j] == '*':
            print(i+1+1, j+1)
            heart = [i+1, j]

            # 왼쪽 팔 구하기
            for k in range(j):
                if cookie[i+1][k] == '*':
                    print(j-k, end=" ")
                    break

            # 오른 팔 구하기
            for k in range(N-1, j, -1):
                if cookie[i+1][k] == '*':
                    print(k-j, end=" ")
                    break

            # 허리 구하기
            for k in range(N-1, i+1, -1):
                if cookie[k][j] == '*':  # 허리
                    print(k-i-1, end=" ")
                    # 왼쪽 다리 k, j-1
                    for l in range(N-1, k, -1):
                        if cookie[l][j-1] == '*':
                            print(l-k, end=" ")
                            break

                    # 오른쪽 다리 k, j+1
                    for l in range(N-1, k, -1):
                        if cookie[l][j+1] == '*':
                            print(l-k, end=" ")
                            break

                    exit(0)