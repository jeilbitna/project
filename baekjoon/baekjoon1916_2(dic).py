import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def solve():
    n = int(input())
    m = int(input())

    graph = [dict() for _ in range(n+1)]

    for _ in range(m):
        start, end, cost = map(int,input().split())
        if end in graph[start]:
            graph[start][end] = min(graph[start][end], cost)
        else:
            graph[start][end] = cost

    origin, destination = map(int,input().split())
    
    def dijkstra():
        costs = [float('inf') for _ in range(n+1)]
        costs[origin] = 0
        q = []
        heappush(q, (0,origin))

        while q:
            current_cost, current_station = heappop(q)
            if costs[current_station] < current_cost:
                continue
            if current_station == destination: # 지금 역이 목표 역이면
                print(current_cost)
                exit()
            
            for new_station, new_cost in graph[current_station].items():
                new_cost += cost
                if new_cost < costs[new_station]:
                    costs[new_station] = new_cost
                    heappush(q,(new_cost,new_station))

    dijkstra()

if __name__ == '__main__':
    solve()