def solution(n):
    ans = 0

    while n > 0:
        n, mod = divmod(n, 2)
        if mod != 0:
            ans += 1

    return ans