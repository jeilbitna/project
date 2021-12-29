# 당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500,100,50,10원이 무한히 존재한다.
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라. ( 단, N은 항상 10의 배수)

# 그리디 알고리즘
import sys

N = int(sys.stdin.readline()) # 거슬러 줘야할 돈
coin = [500,100,50,10] # 거스름돈 동전 리스트
answer = 0

for i in coin:
    if N > i:
        answer += (N//i)
        N = (N % i)

print(answer)