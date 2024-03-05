import sys
input = sys.stdin.readline

T = int(input())
for test in range(T):
    result = [1e9, -1]

    W = input()
    K = int(input())

    for i in range(len(W)):
        for j in range(2, len(W) - i):
            temp = W[i:i+j]
            # K개 가진 알파벳 확인
            flag = False
            for k in range(ord("a"), ord("z")+1):
                # print(temp, temp.count(chr(k)), chr(k))
                if temp.count(chr(k)) == K:
                    if result[0] > len(temp):
                        # print("min: ", temp)
                        result[0] = len(temp)
                    if temp[0] == chr(k) and temp[0] == temp[-1] and result[1] < len(temp):
                        # print("max: ", temp)
                        result[1] = len(temp)
    if result[0] != 1e9 and result[1] != -1:
        print(result[0], result[1])
    else:
        print(-1)