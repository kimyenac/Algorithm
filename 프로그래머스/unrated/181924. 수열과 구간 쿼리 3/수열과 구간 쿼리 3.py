def solution(arr, queries):
    for i, j in queries:
        i_value = arr[i]
        j_value = arr[j]
        arr[i] = j_value
        arr[j] = i_value
    return arr