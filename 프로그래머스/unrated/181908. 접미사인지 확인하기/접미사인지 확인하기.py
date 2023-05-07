def solution(my_string, is_suffix):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[i:])
    return 1 if is_suffix in answer else 0