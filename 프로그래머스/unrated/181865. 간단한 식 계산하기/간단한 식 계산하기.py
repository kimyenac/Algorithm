def solution(binomial):
    answer = binomial.split()
    
    if answer[1] == '+':
        return int(answer[0]) + int(answer[2])
    
    if answer[1] == '-':
        return int(answer[0]) - int(answer[2])
    
    return int(answer[0]) * int(answer[2])