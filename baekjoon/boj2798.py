# 블랙잭 : 합이 21을 넘지 않으면서 카드의 합을 최대한 크게 만드는 게임.

import sys

input = sys.stdin.readline
n, m = map(int, input().split())

cards = list(map(int, input().split()))
cards.sort(reverse=True) # 크기가 100인 정렬 -> O(nlogn) -> 200정도 연산
# n : 카드의 개수, m : 총합 상한선

c = []
for x in range(n):
    for y in range(x+1,n):
        for z in range(y+1,n):
            cardSum =  cards[x]+cards[y]+cards[z]
            if cardSum <= m:
                c.append(cardSum)

print(max(c))
