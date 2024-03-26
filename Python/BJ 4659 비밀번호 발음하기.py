import sys

input = sys.stdin.readline

mo = {"a", "e", "i", "o", "u"}

while True:
    password = input().strip()
    if password == "end":
        break

    if "a" in password or "e" in password or "i" in password or "o" in password or "u" in password:
        m_cnt = 0
        j_cnt = 0
        flag = False

        for i, p in enumerate(password):
            if i > 0:
                if p == password[i - 1] and p != "e" and p != "o":
                    flag = True
                    break
            if p in mo:
                m_cnt += 1
                j_cnt = 0
                if m_cnt == 3:
                    flag = True
                    break
            else:
                m_cnt = 0
                j_cnt += 1
                if j_cnt == 3:
                    flag = True
                    break

        if flag:
            print("<" + password + "> is not acceptable.")
        else:
            print("<" + password + "> is acceptable.")
    else:
        print("<" + password + "> is not acceptable.")
