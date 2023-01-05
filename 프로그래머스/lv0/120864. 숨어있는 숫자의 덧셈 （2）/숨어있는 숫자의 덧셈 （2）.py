def solution(my_string):
    answer = 0
    ans = ''
    for str in my_string:
        if (str.isdigit()):
            ans += str
        else:
            if (ans):
                answer += int(ans)
                ans = ''
    if (ans):
        answer += int(ans)
    return answer