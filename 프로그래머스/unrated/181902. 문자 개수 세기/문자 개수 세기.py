def solution(my_string):
    answer = []
    
    # 대문자
    for i in range(65, 91):
        s = chr(i)
        answer.append(my_string.count(s))
        
    # 소문자
    for i in range(97, 123):
        s = chr(i)
        answer.append(my_string.count(s))
        
    return answer