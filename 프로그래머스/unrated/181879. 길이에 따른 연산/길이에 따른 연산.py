import math

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    return math.prod(num_list)