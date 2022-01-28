import sys
from collections import deque
input = sys.stdin.readline

def bfs(i,j):
    q = deque()
    q.append((i,j))

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = 0

while True:
    w, h = map(int,input().split()) # w = 너비, h = 높이
    graph = []
    cnt = 0
    dx = [-1,1,0,0,1,1,-1,-1]
    dy = [0,0,-1,1,1,-1,1,-1]
    
    if w == 0 and h == 0:
        break

    else:
        for _ in range(h):
            graph.append(list(map(int,input().split())))
        
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    bfs(i,j)
                    cnt += 1
        print(cnt)