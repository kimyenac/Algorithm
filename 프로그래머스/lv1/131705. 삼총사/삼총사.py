from itertools import combinations

def solution(number):
    answer = []
    for i in combinations(number, 3):
        answer.append(sum(i))
    return answer.count(0)