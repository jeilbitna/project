import sys
input = sys.stdin.readline

sh, sm = map(int, input().split())
timer = int(input())

ph = timer // 60
pm = timer % 60

eh = sh + ph
em = sm + pm

if em >= 60:
    em %= 60
    eh += 1

if eh>=24:
    eh %= 24

print(eh,em,sep=' ')