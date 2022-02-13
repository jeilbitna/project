import sys
import heapq
input = sys.stdin.readline

# 목표 : 출발 도시에서 도착 도시까지 가는 데 드는 최소 비용

n = int(input()) # 도시 개수
m = int(input()) # 버스 개수
costs = [float('inf') for _ in range(n+1)] #
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int,input().split())
    graph[start].append((cost,end))

origin, destination = map(int,input().split())

def solve1916(start):
    costs[start] = 0
    q = []
    heapq.heappush(q, (0,start))

    while q:
        current_cost, current_station = heapq.heappop(q)
        if costs[current_station] < current_cost:
            continue

        for new_cost, new_station in graph[current_station]:
            cost = current_cost + new_cost    
            if cost < costs[new_station]:
                costs[new_station] = cost
                heapq.heappush(q, (cost,new_station))

solve1916(origin)
# 정답 출력
print(costs)
print(costs[destination])