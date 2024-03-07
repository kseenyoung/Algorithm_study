import sys
input = sys.stdin.readline

mo = set(["a", "e", "i", "o", "u"])
ja = set(["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"])

while(True):
    password = input().strip()
    if(password == "end"):
        break
    if "a" in password or "e" in password or "i" in password or "o" in password or "u" in password:
        countRepeat = 0
        check = -1  # 1 : 모음, 2 : 자음
        flag = False
        for idx, p in enumerate(password):
            # p가 모음인지 자음인지 & 연속되는가?
            if p in mo:
                if check == 1:
                    if countRepeat == 2:
                        flag = True
                        break
                    else:
                        if password[idx] == password[idx-1] and password[idx] != "o" and password[idx] != 'e':
                            print("<" + password + "> is not acceptable.")
                        countRepeat += 1
                check = 1
            else:
                if check == 2:
                    if countRepeat == 2:
                        flag = True
                        break
                    else:
                        if password[idx] == password[idx - 1]:
                            print("<" + password + "> is not acceptable.")
                        countRepeat += 1
                check = 2

        if flag:
            print("<" + password + "> is not acceptable.")
        else:
            print("<"+password+"> is acceptable.")
    else:
        print("<"+password+"> is not acceptable.")
