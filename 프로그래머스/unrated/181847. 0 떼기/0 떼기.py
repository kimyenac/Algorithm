def solution(n_str):
    answer = ''
    for s in n_str:
        if s != '0' or len(answer) > 0:
            answer += s
    return answer