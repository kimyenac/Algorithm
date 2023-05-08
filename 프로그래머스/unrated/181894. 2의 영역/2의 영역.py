def solution(arr):
    min_idx = -1
    max_idx = 0
    
    for i in range(len(arr)):
        if arr[i] == 2:
            if min_idx > -1:
                max_idx = i
            else:
                min_idx = i
                
    if min_idx == -1:
        return [-1]
    
    if max_idx == 0:
        return [2]
    
    return arr[min_idx:max_idx+1]