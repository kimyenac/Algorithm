def solution(a, b):
    answer = [int(str(a) + str(b)), int(str(b) + str(a))]
    return max(answer)