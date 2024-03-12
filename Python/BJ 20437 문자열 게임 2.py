import sys
from collections import defaultdict
input = sys.stdin.readline

for test in range(int(input())):
    result = [10000, -1]

    W = input().rstrip()
    K = int(input())

    # W에 속하는 알파벳
    alphabets = list(map(lambda x : ord(x) - 97, W.strip()))  # [18, 20, 15, 4, 17, 0, 16, 20, 0, 19, 14, 17, 13, 0, 3, 14]
    dic = defaultdict(list)
    for idx, alpha in enumerate(alphabets):
        dic[alpha].append(idx)  # 해당 알파벳 번호의 발견 위치들 저장

    # 저장된 알파벳의
    for alpha_list in dic.values():
        # 해당 알파벳의 개수가 K개 이상일 때만 진행
        if len(alpha_list) >= K:
            for j in range(len(alpha_list) - K + 1):
                # j : 윈도우의 크기
                alpha_len = alpha_list[j + K - 1] - alpha_list[j] + 1
                if alpha_len < result[0]:
                    result[0] = alpha_len
                if alpha_len > result[1]:
                    result[1] = alpha_len
    if result[0] == 10000 or result[1] == -1:
        print(-1)
    else:
        print(result[0], result[1])