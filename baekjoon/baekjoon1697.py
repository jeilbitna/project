from collections import deque

# n = 5, k = 17 일때 -> 5 - 10 - 9 - 18 - 17
n, k = map(int,input().split()) # n = 출발, k = 도착
q = deque()
maximum = 10 ** 5 # 최대 = 100,000
cnt = [0 for _ in range(maximum+1)]

q.append(n)

while q:
    now = q.popleft()
    if now == k:
        print(cnt[now])
        break

    for next in (now*2,now-1,now+1):
        if 0 <= next <= maximum and not cnt[next]:
            cnt[next] = cnt[now] + 1
            q.append(next)