def solution(n, lost, reserve):
    _lost = sorted([i for i in lost if i not in reserve])
    _reserve = sorted([i for i in reserve if i not in lost])
    answer = n - len(_lost)
    for i in _lost:
        for j in range(-1, 2, 1):
            if j == 0:
                continue
            elif i+j in _reserve:
                    answer += 1
                    _reserve.pop(_reserve.index(i+j))
                    break
    return answer