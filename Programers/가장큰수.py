def solution(numbers):
    answer = ''
    temp_number = []
    ind = 0

    for number in numbers:
        number = str(number)
        if number!= 0:
            i = 0
            while  int(number) < 10000:
                if number =='0':
                    break
                number += number[i]
                i += 1
                if i >= len(number):
                    i =0
            number = int(number)
        temp_number.append([number,ind])
        ind += 1

    temp_number.sort(key = lambda x: (x[0]))
    temp_number.reverse()
    temp_answer = []
    for i in range(len(numbers)):   
        answer += str(numbers[temp_number[i][1]])

    return str(int(answer))