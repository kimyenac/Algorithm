def solution(my_string):
    answer = []
    for str in my_string:
        if str not in answer:
            answer.append(str)
    return "".join(answer)