import math

def solution(n):
    answer = 1
    ans = 0
    while True:
        if (math.factorial(answer) == n):
            return answer
        if (math.factorial(answer) > n):
            return answer - 1
        answer += 1