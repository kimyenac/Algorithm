def solution(n, s):
    answer = []
    
    base = s // n
    rem = s % n
    
    if base == 0: return [-1]
    for i in range(n-rem):
        answer.append(base)
    for i in range(rem):
        answer.append(base+1)
        
    answer.sort()
    
    return answer