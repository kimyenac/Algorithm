def solution(my_string, num1, num2):
    answer = ''
    num1_str = my_string[num1]
    num2_str = my_string[num2]
    for i in range(len(my_string)):
        if i == num1:
            answer += num2_str
        elif i == num2:
            answer += num1_str
        else:
            answer += my_string[i]
    return answer