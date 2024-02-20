word = input()
alp = dict()

for i in range(97, 123):
    alp[chr(i)] = 0

for w in word:
    if w.isupper():
        alp[w.lower()] += 1
    else:
        alp[w] += 1

alp = sorted(alp.items(), key=lambda x:x[1], reverse=True)

if alp[0][1] == alp[1][1]:
    print("?")
else:
    print(alp[0][0].upper())