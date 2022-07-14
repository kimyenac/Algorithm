import math
def solution(begin, end):
    answer = []
    
    for i in range(begin, end+1):
        if i == 1:
            answer.append(0)
        else:
            for j in range(2, int(math.sqrt(i))+1):
                m = i // j
                if m > 10 ** 7:
                    continue
                if i % j == 0:
                    answer.append(m)
                    break
            else:
                answer.append(1)
                    
    return answer