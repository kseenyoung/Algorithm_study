N = int(input())
i = 1
tmp = 1

while 1:
    if N <= tmp:
        break
    tmp += 6*i
    i += 1

print(i)

