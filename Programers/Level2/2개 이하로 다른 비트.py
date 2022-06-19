def solution(numbers):
    answer = []
    for num in numbers:
        if num %2 == 0:
            answer.append(num+1)
        else:
            bit = list(bin(num)[2:])   
            bit = bit[::-1]
            if '0' in bit:
                ind = bit.index('0')
            else:
                ind = 0
            if ind == 0:
                bit = bit[:-1] + ["0",'1'] 
            else:
                bit[ind] = '1'
                bit[ind-1] = '0'
            
        
            
            bit = bit[::-1]
            bit = '0b'+''.join(bit)
            
            answer.append(int(bit,2))
            
    return answer


'''
xor로 해결해 보려 했으나 시간초과로 인해 실패
짝수와 홀수로 나누어 규칙을 발견해야함
짝수는 무조건 제일 뒤 비트가 0이기 때문에 1을 더하면 다른숫자 개수가 1이됨
홀수는 마지막으로 등장하는 0을 1로 바꾸고 그 다음 1을 0으로 바꾸면 됨
홀수의 경우 리스트를 뒤집고 0의 index를 찾아 문제를 해결
'''