def solution(id_list, report, k):
    reported = [0 for _ in range(len(id_list))]
    reports = []
    reporter = [[]for _ in range(len(id_list))]
    check = 0
    answer = [0 for _ in range(len(id_list))]
    for i in range(len(report)):
        temp = map(str, report[i].split())
        
        reports.append(list(temp))
    for i in range(len(id_list)):
        for R in reports:
            if R[0] == id_list[i]:
                reporter[i].append(R[1])
        reporter[i] = list(set(reporter[i]))
    reported_member = sum(reporter,[])
    for i in range(len(id_list)):
        if id_list[i] in reported_member:
            reported[i] = reported_member.count(id_list[i])
    for i in range(len(id_list)):
        if reported[i] >= k:
            reported[i] = 1
        else:
            reported[i] = 0
    
    for i in range(len(id_list)):
        for reported_id in reporter[i]:
            if reported[id_list.index(reported_id)] == 1:
                answer[i] += 1
        
    return answer

a = ["con", "ryan"]
b = ["ryan con", "ryan con", "ryan con", "ryan con"]
c = 3
print(solution(a,b,c))