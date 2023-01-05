def solution(my_string):
    answer = 0
    ans = ''
    for str in my_string.split(" "):
        if str.isdigit() and ans:
            if (ans == '+'):
                answer += int(str)
            elif (ans == '-'):
                answer -= int(str)
            ans = ''
        elif str.isdigit() and not ans:
            answer = int(str)
        else:
            ans = str 
    return int(answer)