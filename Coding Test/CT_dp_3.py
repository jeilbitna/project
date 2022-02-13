import sys
input = sys.stdin.readline

n = int(input()) # 식량 창고의 개수 ( 3 <= n <= 100)
array = list(map(int,input().split())) # 각 식량창고에 저장된 식량의 개수
dp = [0] * 100 # dp 테이블

dp[0] = array[0]
dp[1] = max(array[0], array[1])

for i in range(2,n):
    dp[i] = max(dp[i-1], dp[i-2] + array[i])

print(dp[n-1])
