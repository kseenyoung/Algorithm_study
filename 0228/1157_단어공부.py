import sys

string = sys.stdin.readline().strip().upper() # 대문자로 치환

alpha = set(string) # 알파벳 종류
dict = {}

for a in alpha:
    dict[a] = string.count(a) # 각 알파벳 몇번 나왔나

max_cnt = max(list(dict.values())) # 제일 많이 나온 횟수
result = ""
for key in dict.keys(): # 알파벳 돌면서
    if dict[key] == max_cnt: # 제일 많이 나온 알파벳이고
        if result == "": # 처음 나온 애면
            result = key # 결과에 저장
        else: # max가 같은 애가 있으면
            result = "?" 
print(result)
