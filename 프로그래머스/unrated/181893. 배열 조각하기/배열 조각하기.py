def solution(arr, query):
    for i in range(len(query)):
        idx = query[i]
        if i % 2 == 0:
            arr = arr[:idx+1]
        else:
            arr = arr[idx:]
    return arr