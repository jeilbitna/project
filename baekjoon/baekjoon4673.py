num_list = set(range(1,10001)) # 1부터 1만까지 자연수
sn_list = set() # 셀프 넘버

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    sn_list.add(i)

result = sorted(num_list - sn_list)

for x in result:
    print(x)