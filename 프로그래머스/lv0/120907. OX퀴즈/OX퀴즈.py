def solution(quiz):
    answer = []
    for x in quiz:
        math_list = x.split()
        if math_list[1] == '-':
            ans = int(math_list[0]) - int(math_list[2])
        else:
            ans = int(math_list[0]) + int(math_list[2])
        if str(ans) == math_list[-1]:
            answer.append("O")
        else:
            answer.append("X")
    return answer