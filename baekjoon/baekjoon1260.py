import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int,input().split()) # n = 정점 개수, m = 간선 개수, v = 탐색 시작 번호
graph = [[] for _ in range(n+1)] # 간선 정보가 입력되면 노드 연결 정보로 옮길 곳
visited = [False for _ in range(n+1)]
dfs_result = []
bfs_result = []
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for node in graph:
    node.sort()

def dfs(v,graph,visited):
    visited[v] = True # 방문 처리
    dfs_result.append(v)
    for node in graph[v]:
        if not visited[node]: # 방문하지 않았다면
            dfs(node,graph,visited) # 해당 node를 재귀함수로 다시 방문
    return dfs_result

def bfs(v,graph,visited):
    visited = [False for _ in range(n+1)]
    visited[v] = True # 방문 처리
    queue = deque([v]) # 시작점으로 시작
    while queue:
        now = queue.popleft()
        bfs_result.append(now)
        for node in graph[now]:
            if not visited[node]:
                queue.append(node)
                visited[node] = True
    return bfs_result

print(*dfs(v,graph,visited))
print(*bfs(v,graph,visited))