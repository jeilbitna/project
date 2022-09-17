# 오큰수

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
stack = []
answer = []
for i in range(n): # i : 0 ~ n-1
    