import sys

p = int(sys.stdin.readline().strip())

for _ in range(p):
    data = list(map(int, sys.stdin.readline().split()))

    result = 0
    for i in range(1, len(data) - 1):  # 전체 애들 대해
        for j in range(i + 1, len(data)):  # 내 뒷애들 다 봐서
            if data[i] > data[j]:  # 나보다 키크면
                data[i], data[j] = data[j], data[i]  # 자리바꿈
                result += 1
    print(data[0], result)
