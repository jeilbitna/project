import sys
input = sys.stdin.readline
n, m = map(int,input().split()) # n = 세로, m = 가로

lab = []
for _ in range(n):
    lab.append(list(map(int,input().split())))

print(lab)