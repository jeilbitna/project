import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    data = input().rstrip()
    if data not in array:
        array.append(data)

array.sort(key = lambda data: (len(data), ascii(data)))

for data in array:
    print(data)

# 1등의 풀이법
import sys
word=set()
for i in range(int(input())):
    word.add(sys.stdin.readline().rstrip())
word=list(word)
word.sort()
word.sort(key=lambda x:len(x))
print("\n".join(word))
