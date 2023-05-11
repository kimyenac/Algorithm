def solution(str_list, ex):
    answer = ''
    
    for s in str_list:
        isTrue = True
        for i in range(len(s) - len(ex) + 1):
            if s[i:i+len(ex)] == ex:
                isTrue = False
                break
        if isTrue:
            answer += s
    
    return answer