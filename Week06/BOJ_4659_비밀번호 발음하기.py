def isVowel(c):
    if c in ('a', 'e', 'i', 'o', 'u'):
        return True
    return False


def func(pw):
    if 'a' not in pw and 'e' not in pw and 'i' not in pw and 'o' not in pw and 'u' not in pw:
        print("<{}> is not acceptable.".format(''.join(pw)))
        return

    for i in range(len(pw) - 2):
        if isVowel(pw[i]) and isVowel(pw[i + 1]) and isVowel(pw[i + 2]):
            print("<{}> is not acceptable.".format(''.join(pw)))
            return

        if not isVowel(pw[i]) and not isVowel(pw[i + 1]) and not isVowel(pw[i + 2]):
            print("<{}> is not acceptable.".format(''.join(pw)))
            return

    for i in range(len(pw) - 1):
        if pw[i] == pw[i + 1]:
            if pw[i] not in ('e', 'o'):
                print("<{}> is not acceptable.".format(''.join(pw)))
                return

    print("<{}> is acceptable.".format(''.join(pw)))
    return

while 1:
    pw = list(input())
    flag = 0
    if pw == ['e', 'n', 'd']:
        exit(0)
    func(pw)
