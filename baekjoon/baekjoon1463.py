import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

for i in range(2,n+1):
    dp[i] = dp[i-1] + 1 # 1로 나누는 게 제일 안 좋은 방법

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[n])
