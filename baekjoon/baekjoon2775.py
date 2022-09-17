import sys
input = sys.stdin.readline
t = int(input())
dp = [ [0 for _ in range(15)] for _ in range(15) ]

def solve2775(x,y): # k층 n호의 거주자 수 출력 함수
    if y == 1: # 1호이면 무조건 1
        return 1
    
    if x == 1: # 1층인 경우 : 기록하고 출력
        if dp[x][y]:
            return dp[x][y]
        else:
            for i in range(1,y+1):
                dp[x][i] = i*(i+1)//2
            return dp[x][y]
    else: # 2층 이상일 경우
        if dp[x][y]:
            return dp[x][y]
        else:
            for i in range(1,n+1):
                dp[x][y] += solve2775(k-1,i)
            return dp[x][y]

for _ in range(t):
    k = int(input())
    n = int(input())
    result = solve2775(k,n)

    print(result)