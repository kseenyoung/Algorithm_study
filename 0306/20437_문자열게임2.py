import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    w = sys.stdin.readline().strip()
    k = int(sys.stdin.readline().strip())

    dict = {}

    for _ in w:
        dict[_] = dict.get(_, 0) + 1  # get 쓰면 키 없을때 오류 안남

    check = False
    result3 = len(w)
    result4 = -1

    idx_dict = {}  # 해당 문자가 나온 인덱스 저장

    for i in range(len(w)):
        if dict[w[i]] < k:  # k번보다 적게 나왔으면
            continue
        check = True  # 여기 왔으면 일단 답이 있다는거니까
        idx_dict[w[i]] = idx_dict.get(w[i], []) + [i]  # 해당 문자가 나온 인덱스

    for key, val in idx_dict.items():  # 인덱스 돌면서
        for i in range(len(val) - k + 1):  # k개 중심으로 이동
            result3 = min(result3, val[i + k - 1] - val[i] + 1)  # 문자열 길이 최소
            result4 = max(result4, val[i + k - 1] - val[i] + 1)  # 문자열 길이 최대

    if check:
        print(result3, result4)
    else:
        print(-1)
