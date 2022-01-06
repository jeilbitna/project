import sys

N, M = map(int,sys.stdin.readline().split())

result = 0
for _ in range(N):
    card = list(map(int,sys.stdin.readline().split()))
    min_card = 10001 # 범위가 10000까지이므로 무조건 그보다 큰 10001
    for x in card:
        min_card = min(min_card,x) # card 리스트를 돌며 가장 작은 수의 카드 확정
    result = max(min_card,result) # 가장 작은 카드들 중 가장 큰 수의 카드