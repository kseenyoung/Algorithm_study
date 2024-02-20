S = input()
T = input()

def dfs(T):
    global ans
    if len(T) == len(S):
        if T == S:
            print(1)
            exit()
        return

    if T[-1] == 'A':
        dfs(T[0:-1])

    if T[0] == 'B':
        dfs(T[:0:-1])

dfs(T)
print(0)
