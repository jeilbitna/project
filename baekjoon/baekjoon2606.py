import sys
input = sys.stdin.readline

n = int(input()) # 컴퓨터의 수
k = int(input()) # 직접 연결된 컴퓨터 쌍의 수

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)] # 방문 여부

for _ in range(k):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    visited[v] = True # 방문 처리
    for node in graph[v]:
        if not visited[node]:
            dfs(node)

dfs(1)
print(visited.count(True)-1)