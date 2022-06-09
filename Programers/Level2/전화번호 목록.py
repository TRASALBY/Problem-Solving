def solution(phone_book):
    
    phone_book.sort()
    
    for i in range(len(phone_book)):
        num_len = len(phone_book[i])
        for j in range(i+1,len(phone_book)):
            if phone_book[i] == phone_book[j][0:num_len]:
                return False
            else:
                break
        
                  
    return True