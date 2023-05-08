def solution(arr):
    answer = []
    for cnt in arr:
        for i in range(cnt):
            answer.append(cnt)
    return answer