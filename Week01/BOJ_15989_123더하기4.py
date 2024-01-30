import sys
input = sys.stdin.readline

dp = [1]*10001   # 1만 사용해서 나타내는 경우의 수로 초기화
dp[1] = 1


for i in range(2, 10001):   # 전 단계에서 2를 추가하는 경우
    dp[i] += dp[i-2]

for i in range(3, 10001):   # 전 단계에서 3을 추가하는 경우
    dp[i] += dp[i-3]


for _ in range(int(input())):
    print(dp[int(input())])
