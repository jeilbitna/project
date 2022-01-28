import sys
from collections import deque

# 기본 세팅
input = sys.stdin.readline
v, e = map(int,input().split()) # v = 정점 개수, e = 간선 개수
k = int(input()) # 출발 노드
distances = [float('inf') for _ in range(v+1)] # 최단 거리 기록(테이블)
visited = [False for _ in range(v+1)] # 방문한 노드 기록
graph = [[] for _ in range(v+1)] # 연결 상태
queue = deque()
for _ in range(e):
    v1, v2, w = map(int,input().split()) # u -> v 로 가는 가중치 w인 간선이 존재
    graph[v1].append((v2,w))
    
# 다익스트라
distances[k] = 0 # 출발 노드는 0으로 만듬
for x in graph[k]:
    queue.append((k,x[0],x[1]))
visited[k] = True # 방문 처리

while queue:
    prev_node, next_node, next_weight = queue.popleft()
    if next_weight > distances[next_node]:
        continue
    distance = distances[prev_node] + next_weight
    
    if distance < distances[next_node]:
        distances[next_node] = distance # 갱신
        
        # 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 고름.
        min_value = float('inf')
        index = 0
        for i in range(1,v+1):
            if distances[i] < min_value and not visited[i]:
                min_value = distances[i]
                index = i

        for x in graph[index]:
            queue.append((index,x[0],x[1]))
        visited[index] = True
            
for i in range(1,v+1):
    if distances[i] == float('inf'):
        print('INF')
    else:
        print(distances[i])