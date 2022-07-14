def solution(citations):
    answer = []
    citations.sort()
    n = len(citations)
    for h in range(n+1):
        ans1, ans2 = 0, 0
        for i in range(n):
            if ans2 > h:
                break
            if h <= citations[i]:
                ans1 += 1
            else:
                ans2 += 1
        if h <= ans1 and h >= ans2:
            answer.append(h)
    return max(answer)