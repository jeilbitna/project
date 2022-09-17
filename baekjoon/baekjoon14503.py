import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
    
n, m = map(int,input().split()) # n : 세로 크기, m : 가로 크기

r, c, d = map(int,input().split())
arr = [[] for _ in range(n)]
dx = [-1,0,1,0] # 북,동,남,서 순
dy = [0,1,0,-1] # 북,동,남,서 순
result = 0


for i in range(n):
    arr[i] = list(map(int,input().split()))

def solve(x,y,d):
    global result
    if arr[x][y] == 0: # 청소 안 되어 있으면
        arr[x][y] = -1 # 청소
        result += 1 # 청소 횟수 증가
    
    cannot = 0
    for _ in range(4):
        nd = (d+3) % 4
        nx, ny = (x + dx[nd]), (y + dy[nd])

        if arr[x][y] == -1:
            if arr[nx][ny] == 0:
                solve(nx,ny,nd)
                break

            else:
                d = nd
                cannot += 1
    
    if cannot == 4:
        nd = (d+2) % 4
        nx, ny = (x + dx[nd]), (y + dy[nd])

        if arr[nx][ny] == 1: # 뒤쪽이 벽이면
            return
        
        else:
            solve(nx,ny,d)

solve(r,c,d) # 시작
print(result)
