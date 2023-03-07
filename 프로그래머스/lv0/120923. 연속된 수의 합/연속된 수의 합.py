def solution(num, total):
    ans = -num
    while True:
        x = ans
        for i in range(1, num):
            x += ans + i
        if (x == total):
            return [i for i in range(ans, num+ans)]
        ans += 1