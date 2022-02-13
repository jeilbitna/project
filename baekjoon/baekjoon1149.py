import sys
input = sys.stdin.readline

n = int(input()) # 2 <= n <= 1,000
rgb = []

for _ in range(n):
    rgb.append(list(map(int,input().split())))

for i in range(1,n):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

print(min(rgb[n-1][0], rgb[n-1][1], rgb[n-1][2]))

# 만약 i번째 집에 r/g/b중 한 색을 칠한다면, i-1번째 집에는 그 색을 제외한 나머지 두 색을 칠할 수 있음.

# 그 두 색 중에서 적은 비용이 드는 것을 채택(min 함수) 하고, i번째 집에 칠하는 색의 비용을 더함.
# (이러면 구조상 기존 rgb 리스트 안의 i번째 리스트는, 1~i번째까지의 비용의 총합이 누적되게 됨.)

# 반복문이 끝나면, n-1번째(인덱스 상으로) 리스트에는 총 누적값들이 쌓임. 이 중 최소를 고르면 정답.