import sys
input = sys.stdin.readline

n, c = map(int,input().split())
house = []

for _ in range(n):
    house.append(int(input()))

result = 0 # 정답
start = 0
end = max(house)
house.sort()

while (start <= end):
    
    mid = (start + end) // 2 # 최소 간격을 설정한다.
    cnt = 1 # 와이파이 설치 개수. 처음 집에 하나 설치한다 가정하므로 1부터 시작
    now = house[0] # now는 마지막으로 와이파이가 설치된 집을 의미. 처음 집에 하나 설치하므로 house[0] 로 설정한다.
    
    for i in range(1,n):
        if (house[i] - now) >= mid:
            now = house[i] # 현재 설치된 집
            cnt += 1 # 설치 개수 추가
            
    if cnt >= c:
        if result < mid:
            result = mid
        start = mid + 1

    else:
        end = mid - 1
 
print(result)
