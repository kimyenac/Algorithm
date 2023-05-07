def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        s, e = parts[i]
        answer += my_strings[i][s:e+1]
    return answer