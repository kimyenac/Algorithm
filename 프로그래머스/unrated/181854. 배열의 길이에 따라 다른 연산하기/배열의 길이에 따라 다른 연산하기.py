def solution(arr, n):
    answer = []
    isOdd = len(arr) % 2 != 0
    
    for i in range(len(arr)):
        if isOdd and i % 2 == 0:
            arr[i] += n
        if not isOdd and i % 2 != 0:
            arr[i] += n
    
    return arr