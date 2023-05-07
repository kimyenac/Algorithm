def solution(my_string, indices):
    answer = list(my_string)
    for idx in indices:
        answer[idx] = '0'
    return "".join(answer).replace('0', '')