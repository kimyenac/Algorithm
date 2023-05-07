def solution(intStrs, k, s, l):
    answer = []
    for x in intStrs:
        ans = int(x[s:s+l])
        if (ans > k):
            answer.append(ans)
    return answer