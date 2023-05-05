def solution(a, b, n):
    answer = 0
    
    while n >= a:
        x = n % a
        n = (n // a) * b
        answer += n
        n += x
    
    return answer