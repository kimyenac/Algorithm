def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for x, y in zip(arr1[i], arr2[i]):
            answer[i].append(x + y)
    return answer