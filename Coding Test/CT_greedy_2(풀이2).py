import sys

N, M = map(int,sys.stdin.readline().split())

result = 0

for _ in range(N):
    card = list(map(int,sys.stdin.readline().split()))
    min_card = min(card) # card 리스트 중 가장 작은 카드
    result = max(result, min_card) # 가장 작은 수의 카드들 중 가장 큰 수의 카드를 계속 갱신하는 방식이다.

print(result)