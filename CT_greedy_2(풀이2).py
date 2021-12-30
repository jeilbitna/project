import sys

N, M = map(int,sys.stdin.readline().split())

result = 0

for _ in range(N):
    card = list(map(int,sys.stdin.readline().split()))
    min_card = min(card)
    result = max(result, min_card) # 계속 result를 큰 값으로 갱신하는 방식이다.

print(result)