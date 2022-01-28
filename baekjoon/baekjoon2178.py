import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int,input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    graph.append(list(map(int,input().strip('\n'))))

def escape(x,y):
    q = deque()
    q.append((x,y)) # 시작 좌표
    
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: # 미로 이탈
                continue
            if graph[nx][ny] == 0: # 이동할 수 없는 칸
                continue
            if graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

        
    return graph[n-1][m-1]

print(escape(0,0)) 
