def solution(num_list):
    for num in num_list:
        if (num < 0):
            return num_list.index(num)
    return -1