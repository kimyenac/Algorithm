def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget < i:
            break
        answer += 1
        budget -= i
    return answer