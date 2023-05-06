def solution(str1, str2):
    answer = ''
    for s1, s2 in zip(str1, str2):
        answer += str(s1 + s2)
    return answer