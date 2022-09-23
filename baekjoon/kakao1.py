def solution(id_list, report, k):
    answer = []
    
    report = list(set(report)) # 중복 제거

    
    result = dict(zip(id_list, [0 for _ in range(len(id_list))])) # 신고 당한 횟수
    # result = {muzi : 1, frodo : 2, apeach : 0, neo : 2}
    result2 = dict(zip(id_list, [[] for _ in range(len(id_list))])) # key : 신고당함 / val : 신고함
    # result2 = {muzi : [apeach], frodo : [muzi, apeach], apeach : [], neo : [frodo, nuzi]} # val : 중복 제거 필요?
    result3 = dict(zip(id_list, [0 for _ in range(len(id_list))]))
    
    for rep in report:
        # rep[0] : 신고한 사람 // rep[1] : 신고당한 사람
        p1, p2 = rep.split()[0], rep.split()[1]
        result[p2] += 1
        result2[p2] += [p1]
    
    print("result : {}".format(result))
    print("result2 : {}".format(result2))


    for key, val in result.items():
        if result[key] >= k:
            for id in list(set(result2[key])): # 중복 제거 필요한가
                result3[id] += 1

    for id in id_list:
        answer.append(result3[id])
    
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))