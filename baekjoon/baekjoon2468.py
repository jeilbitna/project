import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
maximum = 0
result = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,h,area):
    q = deque()
    q.append((x,y))
    area[x][y] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if area[nx][ny] <= h:
                continue
            if area[nx][ny] > h:
                q.append((nx,ny))
                area[nx][ny] = 0

for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)
    if maximum < max(row):
        maximum = max(row) # 최대

for k in range(0,maximum+1): # 비가 안오는 경우도 포함해야 하므로 0부터 시작 -> graph에서 가장 큰 수인 maximum까지 돌린다.
    cnt = 0
    area = [item[:] for item in graph]
    for i in range(n):
        for j in range(n):
            if area[i][j] > k:
                bfs(i,j,k,area)
                cnt += 1
    
    result.append(cnt)
print(max(result))