from collections import deque
import sys

n, m = map(int,sys.stdin.readline().split()) # n = 세로, m = 가로
maze = [] # 미로 정의. 괴물이 있으면 0, 없으면 1

for _ in range(n):
    maze.append(list(map(int,sys.stdin.readline().strip('\n')))) 

# 순서대로 상,하,좌,우 이동을 정의한다.
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 탈출 함수 구현(bfs)
def escape(x,y):
    queue = deque() # bfs 돌릴 큐 정의
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] # 이동할 좌표 정의
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m: # 범위 벗어나면
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))
    
    return maze[n-1][m-1] # 큐를 다 돌리고 난 다음에 도착점 값 반환(도착점 값 = 거리 값)
    
print(escape(0,0))
# 출발점(1,1) -> 도착점(n,m) => maze[0][0] => maze[n-1][m-1]
# 막다른 길로 가버린다면? -> *애초에 다음 가는 곳의 값을 +1씩 거리가 증가한 형태로 바꿔버리면, 막다른 길 고려가 필요 없이 찾을 수 있다.
# 따라서 도착점 maze[n-1][m-1] 의 값이 이동한 거리가 되어버린다.
# 단, 시작점(maze[0][0])은 3으로 변경된다. maze[0][1] = 2에서 시작점의 값은 1이므로 시작점은 3으로 바뀐다.