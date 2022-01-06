import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
graph = [ [] for _ in range(n)] # 얼음 틀
count = 0 # 생성되는 아이스크림의 개수

for i in range(n):
    graph[i] = list(map(int,sys.stdin.readline().strip('\n')))

# DFS
def dfs(x,y):
    if x<=-1 or x>= n or y<=-1 or y>=m:
        return False # 즉시 종료(함수에서 return이 되면 종료)

    if graph[x][y] == 0: # 미방문 시
        graph[x][y] = 1 # 방문으로 바꾼다.
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True

    return False

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            count += 1
print(count)