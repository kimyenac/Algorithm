from collections import deque
def win(n, info):
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    max_score = 0
    while q:
        focus, arrow = q.popleft()
        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if lion > apeach:
                gap = lion - apeach
                if max_score > gap:
                    continue
                if max_score < gap:
                    max_score = gap
                    res.clear()
                res.append(arrow)
        elif sum(arrow) > n:
            continue
        elif focus == 10:
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
        else:
            tmp = arrow.copy()
            tmp[focus] = info[focus]+1
            q.append((focus+1, tmp))
            tmp1 = arrow.copy()
            tmp1[focus] = 0
            q.append((focus+1, tmp1))
    return res

def solution(n, info):
    winList = win(n, info)

    if not winList:
        return [-1]
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]