import sys
from collections import deque

input = sys.stdin.readline
n = int(sys.stdin.readline())
graph = []
result = []

def bfs(i,j):
    graph[i][j] = 0
    queue = deque()
    queue.append((i,j))
    count = 1
    while queue:
        x,y = queue.popleft()
        if x+1 < n and graph[x+1][y] == 1:
            count += 1
            queue.append((x+1,y))
            graph[x+1][y] = 0
        if x-1 >= 0 and graph[x-1][y] == 1:
            count += 1
            queue.append((x-1,y))
            graph[x-1][y] = 0
        if y+1 < n and graph[x][y+1] == 1:
            count += 1
            queue.append((x,y+1))
            graph[x][y+1] = 0
        if y-1 >= 0 and graph[x][y-1] == 1:
            count += 1
            queue.append((x,y-1))
            graph[x][y-1] = 0
    result.append(count)
for _ in range(n):
    graph.append(list(map(int,input().strip('\n'))))


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)

result.sort()
print(len(result))
for x in result:
    print(x)