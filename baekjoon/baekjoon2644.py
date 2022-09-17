from collections import deque
import sys
input = sys.stdin.readline

n = int(input()) # 사람 수(노드)
a,b = map(int,input().split()) # 촌수 계산 필요 번호
m = int(input()) # 관계 수(간선)

graph = [ [] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split()) # x는 y의 부모
    graph[x].append(y)
    graph[y].append(x)

q = deque([a])
visited[a] = True
result = [-1 for _ in range(n+1)]
result[a] = 0

while q:
    now = q.popleft()

    for node in graph[now]:
        if not visited[node]:
            visited[node] = True
            q.append(node)
            result[node] = result[now] + 1

print(result[b])