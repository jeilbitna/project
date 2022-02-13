# 한수 = 어떤 양의 정수 x의 각 자리가 등차수열을 이루면, x를 한수라고 함.
n = int(input()) # 1 <= n <= 1,000
han_num = set()

for num in range(1,n+1):
    if num < 100:
        han_num.add(num)
    else:
        if (int(str(num)[0]) - int(str(num)[1])) == (int(str(num)[1]) - int(str(num)[2])):
            han_num.add(num)

print(len(han_num))