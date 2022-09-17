# 덩치

import sys
input = sys.stdin.readline

n = int(input())
information = []
ranks = []

for _ in range(n):
    w,h = map(int,input().split())
    information.append((w,h))


for me in information:
    rank = 1
    for other in information:
        if me == other:
            continue
        if me[0] < other[0] and me[1] < other[1]:
            rank += 1
    
    ranks.append(rank)

for rank in ranks:
    print(rank,sep=' ')
