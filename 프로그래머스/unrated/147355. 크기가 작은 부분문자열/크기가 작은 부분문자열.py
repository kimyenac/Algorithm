def solution(t, p):
    answer = []
    
    for i in range(len(t)-len(p)+1):
        answer.append(int(t[i:i+len(p)]))
    
    return sum([1 for i in answer if int(p) >= i])