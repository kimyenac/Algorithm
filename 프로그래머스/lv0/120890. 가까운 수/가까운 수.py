def solution(array, n):
    array.sort()
    answer = [array[0], abs(array[0] - n)]
    for num in array:
        if abs(num - n) < answer[1]:
            answer = [num, abs(num - n)]
    return answer[0]