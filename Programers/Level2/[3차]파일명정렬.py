def solution(files):
    answer = []
    files_sort = []
    
    for file in files:
        head = ''
        num = ''
        tail = ''
        n_start = 0
        for i in range(len(file)):
            if head == '' and file[i].isdigit():
                head = file[:i]
                n_start = i
            if n_start != 0 and not file[i].isdigit():
                num = file[n_start:i]
                tail = file[i:]
                break
        else:
            num = file[n_start:]
        files_sort.append([head,num,tail])
    files_sort = sorted(files_sort, key = lambda x : (x[0].upper(), int(x[1])))
    for file in files_sort:
        answer.append(''.join(file))
    return answer