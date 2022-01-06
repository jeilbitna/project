import sys
input = sys.stdin.readline
def dfs(v):
    visited = [False for _ in range(n+1)]
    visited[v] = True # 방문 처리
    print(v, end=' ')
    next = edges[][1]


def bfs(v):
    return

n, m, v = map(int,input().split()) # n = 정점 개수, m = 간선 개수, v = 탐색 시작 번호
edges = [] # 간선 정보 모아놓는 곳
for _ in range(m):
    edges.append(list(map(int,input().split())))
    edges.sort(key=lambda x:(x[0],x[1]))

dfs(v)
bfs(v)