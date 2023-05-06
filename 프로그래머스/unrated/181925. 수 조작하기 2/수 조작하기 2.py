def solution(log):
    answer = ''
    ans = log[0]
    for num in log[1:]:
        if (ans + 1 == num):
            answer += "w"
        elif (ans - 1 == num):
            answer += "s"
        elif (ans + 10 == num):
            answer += "d"
        else:
            answer += "a"
        ans = num
    return answer