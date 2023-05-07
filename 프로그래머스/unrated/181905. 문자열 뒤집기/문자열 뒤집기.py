def solution(my_string, s, e):
    answer = list(my_string)
    ans = answer[s:e+1]
    answer[s:e+1] = ans[::-1]
    return "".join(answer)