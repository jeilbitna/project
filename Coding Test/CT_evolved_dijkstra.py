
import sys
import heapq

# 기본 세팅
input = sys.stdin.readline
v, e = map(int,input().split()) # v = 정점 개수, e = 간선 개수
k = int(input()) # 출발 노드
distances = [float('inf') for _ in range(v+1)] # 최단 거리 기록(테이블)
visited = [False for _ in range(v+1)] # 방문한 노드 기록
graph = [[] for _ in range(v+1)] # 연결 상태

for _ in range(e):
    v1, v2, w = map(int,input().split()) # u -> v 로 가는 가중치 w인 간선이 존재
    graph[v1].append((w,v2)) # 우선순위 큐를 위해 자리를 바꿔놓음. (가중치가 낮은 것부터 먼저 꺼내기 위해서)

# 다익스트라
def dijkstra(start):
    queue = []
    distances[start] = 0
    heapq.heappush(queue,(distances[start],start)) # (거리,노드)의 튜플 데이터를 삽입(시작 지점이므로 (0,start) 삽입)

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if visited[current_node]: # 방문한 적이 있다면 무시
            continue
        
        for next_distance, next_node in graph[current_node]:
            distance = current_distance + next_distance
            if distance < distances[next_node]:
                distances[next_node] = distance # 갱신
                heapq.heappush(queue, (distance, next_node))
            
            visited[current_node] = True
    
dijkstra(k)

for i in range(1,v+1):
    if distances[i] == float('inf'):
        print('INF')
    else:
        print(distances[i])