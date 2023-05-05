def solution(name, yearning, photo):
    answer = []
    for arr in photo:
        ans = 0
        for x in arr:
            if (x in name):
                idx = name.index(x)
                ans += yearning[idx]
        answer.append(ans)
    return answer