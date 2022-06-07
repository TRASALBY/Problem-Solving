def solution(s):
    answer = ''
    words = s.split(" ")
    for word in words:
        answer += word[:1].upper() + word[1:].lower() + " "
    return answer[:-1]
