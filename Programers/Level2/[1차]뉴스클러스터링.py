def solution(str1, str2):
    answer = 0
    
    str1_arr = []
    str2_arr = []
    
    
    for i in range(len(str1) -1):
        s = str1[i:i+2]
        if s.isalpha():
            str1_arr.append(s.upper())
            
    for i in range(len(str2) -1):
        s = str2[i:i+2]
        if s.isalpha():
            str2_arr.append(s.upper())
            
    if len(str1_arr) < len(str2_arr):
        str1_arr, str2_arr = str2_arr, str1_arr       
    copy1 = str1_arr.copy()
    copy2 = str2_arr.copy()
    

            
    inter_arr = []
    
    for i in str1_arr:
        if i in copy2:
                copy1.remove(i)
                copy2.remove(i)
                inter_arr.append(i)
    union_arr = copy1 + copy2 + inter_arr
    
    if len(union_arr) == 0:
        return 65536
    
    answer = len(inter_arr) / len(union_arr)
    return int(answer * 65536)