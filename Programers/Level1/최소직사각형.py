def solution(sizes):
    x_max = y_max = 0
    for size in sizes:
        if size[0] > x_max:
            x_max = size[0]
        if size[1] > y_max:
            y_max = size[1]
            
    w = max(x_max,y_max)
    
    h_list = []
    for size in sizes:
        h_list.append(size[0])        
        h_list.append(size[1])
    h_list = sorted(list(set(h_list)))
    h_list.reverse()
    for h_temp in h_list:
        count = 0
        for size in sizes:  
            if (size[0] <= w and size[1] <= h_temp) or (size[1] <= w and size[0] <= h_temp):
                count += 1
            
        if count == len(sizes):
            h = h_temp
    return w * h
