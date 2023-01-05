def solution(emergency):
    answer = []
    emergency_sort = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(emergency_sort.index(i) + 1)
    return answer