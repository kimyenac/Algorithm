def solution(myString, pat):
    answer = ''
    
    for x in myString:
        if x == 'A':
            answer += 'B'
        else:
            answer += 'A'
            
    for i in range(len(answer) - len(pat) + 1):
        if answer[i:len(pat)+i] == pat:
            return 1
            
    return 0