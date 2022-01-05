import sys
sys.setrecursionlimit(10**6)

t = int(sys.stdin.readline())

def dfs(graph,x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(graph,x+1,y)
        dfs(graph,x-1,y)
        dfs(graph,x,y+1)
        dfs(graph,x,y-1)
    return

for _ in range(t):
    m, n, k = map(int,sys.stdin.readline().split()) # m = 가로길이, n = 세로길이, k = 배추가 심긴 위치의 개수
    farm = [[0]*m for _ in range(n)] # 배추밭 구현
    count = 0 # 배추흰지렁이 개수
    
    for i in range(k):
        x,y = map(int,sys.stdin.readline().split())
        farm[y][x] = 1 # 배추가 심긴 땅 구현
    
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                dfs(farm,i,j)
                count += 1
    print(count)