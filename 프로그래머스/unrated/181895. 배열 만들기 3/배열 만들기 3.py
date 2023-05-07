def solution(arr, intervals):
    answer = []
    for a, b in intervals:
        for x in arr[a:b+1]:
            answer.append(x)
    return answer