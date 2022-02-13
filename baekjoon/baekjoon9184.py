import sys
input = sys.stdin.readline

# w(a,b,c) 반환값
# 1. a,b,c가 모두 0 이하 -> " 1 " 반환
# 2. a,b,c가 모두 20 초과 -> " w(20,20,20) " 반환
# 3. a<b<c -> " w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c) " 반환
# 4. 나머지 -> " w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1) " 반환
dp = [ [ [0 for _ in range(21)] for _ in range(21) ] for _ in range(21) ]

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return 1048576
    
    else: # 중간 범위
        if dp[a][b][c]:
            return dp[a][b][c]
        if a<b and b<c:
            dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
            return dp[a][b][c]
        
        dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        return dp[a][b][c]
while True:
    x,y,z = map(int,input().split())
    
    if x == -1 and y == -1 and z == -1: # 종료 조건
        break
    
    
    result = w(x,y,z)
    print('w({0}, {1}, {2}) = {3}'.format(x,y,z,result))