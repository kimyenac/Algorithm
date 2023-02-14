def solution(polynomial):
    ans = []
    sum_x = 0
    sum_num = 0
    for x in polynomial.split():
        if ('x' in list(str(x))):
            if (x == 'x'):
                sum_x += 1
            else:
                sum_x += int(str(x)[:-1])
        if (x.isdigit()):
            sum_num += int(x)
    answer = ''
    if (sum_x > 0):
        if (sum_x > 1):
            answer = str(sum_x) + 'x'
        else:
            answer = 'x'
    if (sum_num > 0):
        if (len(answer) == 0):
            answer = str(sum_num)
        else:
            answer += ' + ' + str(sum_num)
    return answer