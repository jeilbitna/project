n = int(input()) # 1 <= n <= 1e9)
result = ''
array = list(map(int,str(n)))

array.sort(reverse=True)

for x in array:
    result += str(x)

print(int(result))