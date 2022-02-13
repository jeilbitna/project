import sys
input = sys.stdin.readline

n = int(input()) # 1로 만들 숫자
result = 0
l = {n} # 여기에 1이 생기면 종료

while 1 not in l:
    t = set() # l을 돌리면서 나온 추가 숫자들은 t에 넣어놓고, 그걸 다시 l로 옮김
    result += 1
    for num in l:
        if (num%3) == 0: t.add(num//3)
        if (num%2) == 0: t.add(num//2)
        t.add(num-1)
    l = t

print(result)
