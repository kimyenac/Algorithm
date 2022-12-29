def solution(array, height):
    answer = 0
    return sum(1 for i in array if i > height)