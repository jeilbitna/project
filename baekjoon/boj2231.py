# N의 분해합 : N + (N을 이루는 각 자리수의 합)
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라고 함 => N = M + (M의 각 자리수)

# 목표 : 자연수 N(1 <= N <= 1,000,000)의 가장 작은 생성자 구하기

# N = M + (M의 각 자리수) => M을 추측하여 가장 작은 놈으로.. ( M < N)
# 생성자가 없는 경우는 0 출력

import sys

input = sys.stdin.readline

n = int(input())
result = 0

def constructor(x):
    const = 0
    x = str(x)
    for i in range(len(x)):
        const += int(x[i])
    return const

for x in range(n):
    if x + (constructor(x)) == n:
        result = x
        break

print(result)