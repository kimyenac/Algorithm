def solution(arr, delete_list):
    answer = []
    for x in arr:
        if x not in delete_list:
            answer.append(x)
    return answer