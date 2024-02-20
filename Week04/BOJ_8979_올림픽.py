N, K = map(int, input().split())
score = []
result = []
grade = 1
i = 1

for _ in range(N):
    score.append(list(map(int, input().split())))

while score:
    score.sort(key=lambda x: x[i], reverse=True)
    count = 0
    for k in range(1, len(score)):
        if score[k][1] == score[0][1]:
            count += 1
        else:
            break
    if count > 0:
        for c in range(count):
            result.append([score[0][0], grade])
            score.pop(0)
        grade += count
    else:
        result.append([score[0][0], grade])
        score.pop(0)
        grade += 1
    i += 1

result.sort(key=lambda x:x[0])
print(result[K-1][1])