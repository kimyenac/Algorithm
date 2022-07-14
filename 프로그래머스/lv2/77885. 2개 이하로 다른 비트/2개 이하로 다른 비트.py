def solution(numbers):
    answer = []
    
    for num in numbers:
        n = list("0" + bin(num)[2:])
        idx = "".join(n).rfind("0")
        n[idx] = "1"
        
        if num % 2 == 1:
            n[idx+1] = "0"
            
        n = "".join(n)
        
        answer.append(int(n, 2))
    
    return answer