import sys

input = sys.stdin.readline

T = int(input())
ans_list = []

def factorial(x):
    s=[1,1]
    for i in range(2,x+1): # 2부터 x까지
        s.append(i*s[i-1])
    return(s[x])

for _ in range(T):
    n , m = map(int,input().split()) # n = 서쪽 다리 개수. m = 동쪽 다리 개수
    ans_list.append(int(factorial(m)/(factorial(n)*factorial(m-n))))
    


for i in ans_list:
    print(i)