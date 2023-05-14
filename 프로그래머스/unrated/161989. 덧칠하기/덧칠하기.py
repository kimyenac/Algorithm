from collections import deque

def solution(n, m, section):
    dq = deque(section)
    answer = 1
    flag = section[0]+m-1
    
    while dq:
        if flag >= dq[0]:
            dq.popleft()
        else:
            answer += 1
            flag = dq[0]+m-1
            
    return answer