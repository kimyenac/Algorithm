def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        day = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            day += 1
        days.append(day)
    total = 1
    for i in range(1, len(days)):
        if days[i] <= days[i-1]:
            total += 1
            days[i] = days[i-1]
        if days[i] > days[i-1]:
            answer.append(total)
            total = 1
    answer.append(total)
    return answer