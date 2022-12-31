def solution(my_string):
    return sum([int(str) for str in my_string if str.isdigit()])