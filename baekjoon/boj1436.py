from email.mime import base
import sys

input = sys.stdin.readline

# N번째 종말의 수를 구하는 것이 문제
N = int(input())

# 첫 번째는 666
if N == 1:
    print(666)

# 두 번째 부터는?
else:
    count = 1
    for i in range(2,N+1):
        base_title = "{0}666".format(i-1) # {0} 자리에 1~N-1 들어감.
        num_of_extra_six_in_row = 0
        
        for k in range(len(base_title)-3):
            if base_title[-4-k] == '6':
                num_of_extra_six_in_row += 1
            else:
                break
        
        count += int(10**num_of_extra_six_in_row)
        if count >= N:
            break

    if num_of_extra_six_in_row > 0:
        base = int(10**num_of_extra_six_in_row)
        count -= base
        base_title = int(base_title) - int(base_title) % base + (N - count-1)

        print(base_title)