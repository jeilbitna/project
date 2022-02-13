import sys
input = sys.stdin.readline

n = int(input()) # 지방의 수 ( 3 <= n <= 10,000 )
requests = list(map(int,input().split())) # 각 지방의 예산 요청 모음( 1 <= requests[i] <= 1e9 )
m = int(input()) # 총 예산 ( n <= m <= 1e9)


if sum(requests) <= m: # 모든 요청이 배정될 수 있는 경우
    print(max(requests))

else:
    start = 0
    end = max(requests)
    result = 0
    while start <= end:
        mid = (start+end) // 2 # 상한액
        total = 0

        for request in requests:
            if request > mid:
                total += mid

            else:
                total += request
        
        if total > m: # 아직도 요구총액이 너무 크므로, 상한가를 더 내려야 금액을 맞출 수 있다.
            end = mid - 1
        
        else: # 요구 총액이 너무 작으므로, 상한가를 올려야 금액을 맞출 수 있다.
            if result < mid:
                result = mid
            start = mid + 1

    print(result)