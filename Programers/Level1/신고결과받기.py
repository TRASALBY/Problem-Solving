def solution(id_list, report, k):
    report_dic = {}
    reported_dic = {}
    count_dic = {}
    n = len(id_list)
    m = len(report)
    answer = [0 for _ in range(n)]
    for id in id_list:
        report_dic[id] = []
        reported_dic[id] = []
        count_dic[id] = 0
    for i in range(m):
        a, b = map(str, report[i].split())
        report_dic[a].append(b)
        reported_dic[b].append(a)
    for id in id_list:
        report_dic[id] = list(set(report_dic[id]))
        reported_dic[id] = list(set(reported_dic[id]))
        count_dic[id] = len(reported_dic[id])
    for id in id_list:
        if count_dic[id] >= k:
            for id2 in id_list:
                if id in report_dic[id2]:
                    answer[id_list.index(id2)] += 1
        
    return answer