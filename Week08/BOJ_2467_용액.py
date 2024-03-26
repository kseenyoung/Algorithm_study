import sys

N = int(input())
arr = list(map(int, input().split()))

start = 0
end = N-1

ans_result = abs(arr[start] + arr[end])  # 양 끝의 합이 제일 작다고 가정
ans_start = start
ans_end = end

while start < end:  # start 와 end 는 만날 수 없음.
    now = arr[start] + arr[end]

    if abs(now) < ans_result: # 현재까지의 ans보다 0에 가까우면 업데이트
        ans_start = start
        ans_end = end
        ans_result = abs(now)

        if now == 0:
            print(arr[ans_start], arr[ans_end])
            exit(0)

    if now > 0:   # 현재 값이 양수면 오른쪽 포인터를 -1
        end -= 1
    else:  # 음수면 왼쪽 포인터를 +1 해준다
        start += 1

print(arr[ans_start], arr[ans_end])