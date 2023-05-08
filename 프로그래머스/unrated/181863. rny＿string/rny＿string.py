def solution(rny_string):
    answer = ''
    for x in rny_string:
        if x == 'm':
            answer += 'rn'
        else:
            answer += x
    return answer