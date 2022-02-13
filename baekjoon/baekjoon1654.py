import sys
input = sys.stdin.readline

k, n = map(int,input().split()) # 1 <= k <= 10,000 // 1 <= n <= 1,000,000 (단, k와 n은 정수이며 항상 k <= n 을 만족한다.)
lines = [] # 랜선 모음
for _ in range(k):
    lines.append(int(input()))

start = 0
end = max(lines)
result = 0 # 정답

while start <= end:
    mid = (start+end) // 2 # 자를 길이(조절할 값)
    total = 0
    
    if mid > 0:
        for line in lines:
            total += (line//mid)
    else:
        result = 1
        break
    
    if total >= n: # 많이 나옴 -> 갯수 줄여야 함 -> mid를 크게 해야함 -> start 조정
        result = mid # 미리 기록해놓기
        start = mid + 1
    else:
        end = mid - 1

print(result)
