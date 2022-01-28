import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True # 방문 표시
    for node in graph[v]:
        if not visited[node]:
            dfs(node)

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)] # 연결 정보
visited = [False for _ in range(n+1)] # 방문 여부
cnt = 0 

for _ in range(m):
    v1, v2 = map(int,input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for v in range(1,n+1):
    if not visited[v]:
        dfs(v)
        cnt += 1
print(cnt)
