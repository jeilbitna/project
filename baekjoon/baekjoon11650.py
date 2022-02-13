import sys
input = sys.stdin.readline

n = int(input())
coordinate = []

for _ in range(n):
    x, y = map(int,input().split())
    coordinate.append((x,y))

coordinate.sort(key=lambda data:(data[0],data[1]))

for x,y in coordinate:
    print(x, y)