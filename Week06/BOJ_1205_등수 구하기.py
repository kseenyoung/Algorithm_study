N, newScore, P = map(int, input().split())
grade = 1
if N > 0:
    score = list(map(int, input().split()))

    if P == N:
        if score[N-1] >= newScore:
            print(-1)
            exit(0)

    for i in range(len(score)):
        if newScore < score[i]:
            grade += 1
        else:
            break
    print(grade)

else:
    print(grade)