import sys

T = int(input())

for _ in range(T):
    W = list(input())
    alp = [[] for _ in range(ord('z')+1)]
    minAns = sys.maxsize
    maxAns = -1

    # 각 알파벳 위치를 담아줌
    for i in range(len(W)):
        alp[ord(W[i])].append(i)

    K = int(input())

    # K = 1 일 때
    if K == 1:
        print(1, 1)
        continue

    for i in range(ord('a'), ord('z')+1):
        # 알파펫을 포함한 문자열이 K개 이상일때만 탐색.
        if len(alp[i]) >= K:
            tmp = alp[i]

            # min 이든 max 이든 어차피 양 끝은 그 문자열이어야 하므로 같은 로직
            for j in range(K-1, len(tmp)):
                minAns = min(tmp[j]-tmp[j-K+1]+1, minAns)
                maxAns = max(tmp[j]-tmp[j-K+1]+1, maxAns)

    # -1 이 아니면 정답 출력함
    if maxAns != -1:
        print(minAns, maxAns)
    else:
        print(maxAns)