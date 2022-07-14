def check(i, n):
    T = "0123456789ABCDEF"
    q, mod = divmod(i, n)
    if q == 0:
        return T[mod]
    else:
        return check(q, n) + T[mod]


def solution(n, t, m, p):
    answer = ""
    x = m * t

    i = 0
    while True:
        if len(answer) >= x:
            break
        answer += check(i, n)
        i += 1

    return answer[p-1::m][:t]