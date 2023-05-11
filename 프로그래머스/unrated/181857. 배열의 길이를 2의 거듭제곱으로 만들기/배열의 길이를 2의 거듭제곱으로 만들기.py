def solution(arr):
    
    while (len(arr)&len(arr)-1) != 0:
        arr.append(0)
    
    return arr