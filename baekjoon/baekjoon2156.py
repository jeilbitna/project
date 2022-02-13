import sys
input = sys.stdin.readline

n = int(input())

s = [-1] * 10001
dp = [-1] * 10001

for i in range(1,n+1):
    s[i] = int(input())

dp[1] = s[1]
dp[2] = s[1] + s[2]
dp[3] = max(dp[2], s[2]+s[3], s[1]+s[3])

for i in range(4,n+1):
    dp[i] = max(dp[i-1],dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])

print(dp[n])