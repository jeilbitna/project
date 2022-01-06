import sys
n = int(sys.stdin.readline())
count = 0 # 그룹 단어의 개수
for _ in range(n):
    already = [] # 이미 나왔던 알파벳들을 모아놓은 리스트
    words = sys.stdin.readline().strip('\n')
    is_groupword = True # 그룹 단어인지 여부 확인
    
    prev = words[0]
    already.append(words[0])
    for i in range(1,len(words)):
        if prev == words[i]: # 연속하는 알파벳인가?
            prev = words[i] # 이전 값 갱신
            continue # 그대로 다음 반복으로
        else: # 연속하지 않는 알파벳
            if words[i] in already: # 연속하지 않는 알파벳인데 이미 already에 들어가있다 = 이미 나왔던 알파벳이다
                is_groupword = False # 그룹 단어가 아님
                break # 종료
            already.append(words[i]) # already에 없다면 최초발견 -> already에 추가
            prev = words[i] # 이전 값 갱신
    if is_groupword: # 그룹 단어이면 count에 추가
        count += 1

print(count) # 출력

"""
이 문제를 보고나서, 문자를 하나하나 돌면서 확인하고, 이미 등장한 문자를 저장할 공간(코드에서 already 리스트)이 필요하다는 생각이 들었습니다.
already에 이미 있는 문자가 나오면 그룹 단어가 아니므로 그 이후는 확인할 필요가 없습니다. 하지만 그렇게만 검증한다면, 예제의 'happy' 같은 단어는
p가 연속해서 나오고, 이 연속하는 p가 단어에서 등장하는 p의 전부입니다. 그러므로 확인 과정을 하나 더 거쳐야 하는데, 저는 다음과 같이 작성했습니다.
1. 이번 알파벳이 이전 알파벳(prev라는 변수에 저장했습니다.)과 같다면 연속해서 나오는 것이므로 prev 값만 갱신해주고 continue로 넘어간다.
2. 이번 알파벳이 이전 알파벳과 다를 때(연속해서 나오는 게 끝났을 때) 이미 나왔던 단어인지(already에 있는지) 확인해보고 있으면 break로 종료. (이미 그룹단어 x => is_groupword = False)
없다면 이번에 나온 알파벳을 already에 넣어줌 + prev 값 갱신.
3. 최종적으로 is_groupword = True 이면 count에 추가
"""