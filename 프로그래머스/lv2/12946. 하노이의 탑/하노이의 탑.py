def solution(n):
    answer = []
    
    def hanoi(n, start, to, via):
        if n == 1:
            answer.append([start, via])
        else:
            hanoi(n-1, start, via, to)
            answer.append([start, via])
            hanoi(n-1, to, start, via)
        
    hanoi(n, 1, 2, 3)
    
    return answer