def solution(ineq, eq, n, m):
    if (eq == "="):
        if (ineq == '<' and n <= m):
            return 1
        if (ineq == '>' and n >= m):
            return 1
    else:
        if (ineq == '<' and n < m):
            return 1
        if (ineq == '>' and n > m):
            return 1
    return 0