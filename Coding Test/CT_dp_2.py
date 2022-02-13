import sys
input = sys.stdin.readline

x = int(input()) # 1<= x <= 30,000
dp = [0] * 30001 # x의 범위가 1에서 3만까지이므로

for i in range(2,x+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i//5] + 1)

print(dp[x])
