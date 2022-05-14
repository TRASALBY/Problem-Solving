def solution(phone_book):
    answer = True
      
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        print(phone_book[i],phone_book[i+1][:len(phone_book[i])])
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
                  
    return answer

solution(["119", "97674223", "1195524421"])