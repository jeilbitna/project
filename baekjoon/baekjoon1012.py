import sys
import networkx as nx 

T = int(sys.stdin.readline())

for _ in range(T):
    
    M, N, K = map(int,sys.stdin.readline().split())
    s = [0] * K # 위치 찾기 리스트
    g = nx.Graph()
    node_list = [0] * K
    
    for i in range(K): # s 정의 + 노드 만들기
        s[i] = list(map(int,sys.stdin.readline().split()))
        g.add_node(i)
        node_list[i] = i

    for i in range(len(s)):
        for j in range(len(s)):
            if ( s[i][0] == s[j][0] and abs(s[i][1] - s[j][1]) == 1 ) or ( s[i][1] == s[j][1] and abs(s[i][0] - s[j][0]) == 1 ):
                g.add_edge(i,j)
    
    count_list=[] # has_path 개수 세주는 리스트

    for i in node_list:
        num_count = 0
        for j in node_list:
            if nx.has_path(g,i,j) == True:
                num_count += 1
        
        count_list.append(num_count-1)
    print(count_list)
    
    answer = 0 # 정답
    for i in range(max(count_list)+1):
        answer += (count_list.count(i) // (i+1))
    
    print(answer)