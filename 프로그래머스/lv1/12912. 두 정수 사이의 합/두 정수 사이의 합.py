def solution(a, b):
    if a > b: b, a = a, b
    return sum(range(a, b+1))