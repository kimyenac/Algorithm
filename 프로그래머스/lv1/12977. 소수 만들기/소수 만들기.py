from itertools import combinations

def check(a, b, c):
    total = a + b + c
    for i in range(2, total):
        if total % i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        if check(i[0], i[1], i[2]):
            answer += 1
    return answer