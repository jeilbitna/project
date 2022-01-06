import sys

N, M = map(int,sys.stdin.readline().split())

card = []

for _ in range(N):
    min_card = min(list(map(int,sys.stdin.readline().split())))
    card.append(min_card)

print(max(card))
    
