# 당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500,100,50,10원이 무한히 존재한다.
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라. ( 단, N은 항상 10의 배수)

# 그리디 알고리즘
import sys

N = int(sys.stdin.readline()) # 1
coin = [500,100,50,10] # 2
answer = 0 # 3

for i in coin: # 4
    if N > i: # 5
        answer += (N//i) # 6
        N = (N % i) # 7

print(answer) # 8

""" <풀이>
1. N을 입력받습니다.
2. 거슬러 줄 동전 개수가 최소가 되어야 하므로, 동전들의 금액을 요소로 하는 coin 리스트를 만들면서도 요소들을 미리 금액의 내림차순으로 만들어 놓습니다.
3. 정답인 answer 입니다.
4. 반복문을 돕니다.
5. N이 거슬러 줄 동전의 액수보다 커야만 하므로 조건을 겁니다.
6. N(거슬러 줘야할 돈)을 i(동전의 금액)로 나눈 몫만큼만 거슬러 줄 수 있습니다.
7. N의 값을 거슬로 주고 남은 돈으로 바꿔줘야 하기 때문에 N을 i로 나눈 나머지로 바꿔줍니다. 
"""