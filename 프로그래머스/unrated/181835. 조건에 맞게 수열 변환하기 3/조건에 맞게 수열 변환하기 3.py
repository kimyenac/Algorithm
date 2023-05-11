def solution(arr, k):
    answer = []
    
    isOdd = k % 2 != 0
    
    for x in arr:
        if isOdd:
            answer.append(x * k)
        else:
            answer.append(x + k)
    
    return answer