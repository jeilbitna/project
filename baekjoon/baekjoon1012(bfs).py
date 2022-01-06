import sys
from collections import deque

t = int(sys.stdin.readline()) # 테스트 케이스의 개수

def bfs(graph,x,y):
    queue = deque([(x,y)]) # 시작
    graph[x][y] = 0 # 방문 처리

    while queue:
        now = queue.popleft() # 해당 좌표
        
        nx,ny = now[0], now[1]
        
        if nx-1 >= 0 and 0 <= ny <= m-1:
            if graph[nx-1][ny] == 1:
                queue.append((nx-1,ny))
                graph[nx-1][ny] = 0
        if nx+1 < n and 0 <= ny <= m-1:
            if graph[nx+1][ny] == 1:
                queue.append((nx+1,ny))
                graph[nx+1][ny] = 0
        if 0 <= nx <= n-1 and ny-1 >= 0:
            if graph[nx][ny-1] == 1:
                queue.append((nx,ny-1))
                graph[nx][ny-1] = 0
        if 0 <= nx <= n-1 and ny+1 < m:
            if graph[nx][ny+1] == 1:
                queue.append((nx,ny+1))
                graph[nx][ny+1] = 0


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
                bfs(farm,i,j)
                count += 1
    print(count)
