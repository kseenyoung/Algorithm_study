import sys
input = sys.stdin.readline

n = int(input())
person = []

for i in range(n):
    x, y = map(int, input().split())
    person.append([x, y, i])

# print(person)
# person.sort(key = lambda x : (-abs((x[0] + x[1])/2), -x[0], -x[1]))
# print(person)

# num = 0
rank = 1
ranking = [1 for i in range(n)]
for i in range(0, n):
    now = person[i]
    for j in range(0, n):
        compare = person[j]
        if compare[0] > now[0] and compare[1] > now[1]:
            rank += 1
    ranking[now[2]] = rank
    rank = 1

for i in range(n):
    print(ranking[i], end=" ")