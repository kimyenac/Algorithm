def solution(a, d, included):
    answer = 0
    ans = a
    for include in included:
        if include:
            answer += ans
        ans += d
    return answer