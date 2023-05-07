def solution(my_string, queries):
    answer = list(my_string)
    for s, e in queries:
        ans = answer[s:e+1]
        answer[s:e+1] = ans[::-1]
    return "".join(answer)