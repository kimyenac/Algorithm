def solution(lines):
    answer = []
    cnt = 0
    for line in lines:
        line.sort()
    for x, y in lines:
        for i in range(x, y):
            if (i not in answer):
                answer.append(i)
            else:
                answer.pop(answer.index(i))
                cnt += 1
            
    return cnt