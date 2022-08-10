def solution(arr):
    arr.pop(arr.index(min(arr)))
    return arr if len(arr) > 0 else [-1]