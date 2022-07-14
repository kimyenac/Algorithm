def solution(n):
    answer = [0, 1, 2]
    
    for i in range(3, n+1):
        answer.append((answer[i-1] + answer[i-2]) % 1234567)
    
    return answer[n]