# bfs 써야할듯?
import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int,input().split()) # m = 가로 길이, n = 세로 길이
graph = [] # 토마토 창고
begin = [] # 익은 토마토들의 위치
count = 0 
# 상,하,좌,우 조작
dx = [-1,1,0,0] 
dy = [0,0,-1,1]

for i in range(n):
    row = list(map(int,input().split()))
    graph.append(row)
    count += row.count(0)
    for j in range(len(row)):
        if row[j] == 1:
            begin.append((i,j))

def bfs(begin):
    q = deque()
    for start in begin:
        q.append(start)    
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

if count == 0: # 저장될 때부터 모든 토마토가 익어있는 상태이면 0 출력
    print(0)
else:
    bfs(begin)
    max_list = [max(i) for i in graph]
    check=[]
    for x in graph:
        if 0 in x:
            check.append(0)
    if 0 in check: # 토마토가 모두 못 익는 상황이면 -1 출력
        print(-1)
    else:
        print(max(max_list)-1)

