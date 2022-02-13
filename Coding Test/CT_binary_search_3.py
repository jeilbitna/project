import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n = 떡의 개수, m = 요청한 떡의 길이 ( 1 <= n <= 1,000,000 // 1 <= m <= 2,000,000,000 )
array = list(map(int, input().split())) # 떡들의 높이
array.sort()
start = 0
end = max(array)
answer = 0 # 정답

while (start <= end):
    mid = (start + end) // 2
    result = 0
    
    for x in array:
        if mid < x:
            result += (x - mid)
        
    # 1. 떡을 목표값보다 많이 자른 경우 -> 절단기 높이를 올려야 함 -> start를 건드림 
    if result >= m:
        # 지금 정답에 절단기 높이를 기록해놓는 이유 ? 최대한 덜 잘랐을 때(절단기 높이가 최대일 때)가 정답이므로.
        # 만약 이 다음번 반복문 실행에서 
        answer = mid
        start = mid + 1
    # 2. 떡을 목표값보다 적게 자른 경우 -> 절단기 높이를 내려야 함 -> end를 건드림
    else:
        end = mid - 1

print(answer)

# 이 while 반복문을 돌 때, 절단기 높이는 너무 많이 잘랐다 싶으면 up(#1), 너무 적게 잘랐다 싶으면 down(#2) 이 두개의 분기점으로 나뉘게 된다.
# 이진 탐색의 특성상, 중간값은 시간이 지날수록 '최적화된 값'을 찾는다. 그리고 구하고자 하는 값은 절단기의 최대 높이이다.
# (왜냐하면 start와 end가 점점 범위를 좁혀 들어오면서 목표 값에 접근해오기 때문이다.)
# 따라서 자른 떡의 총 길이가 필요한 떡의 길이보다 길 때마다 answer에 저장함으로써 갱신해주는 것이다.
# 그렇게 되면 반복문이 종료되었을 때 남아있는 answer의 값이 구하고자 하는 절단기의 최대 높이가 되는 것이다.