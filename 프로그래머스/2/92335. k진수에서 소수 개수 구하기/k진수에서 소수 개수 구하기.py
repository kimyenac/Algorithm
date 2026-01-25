def solution(n, k):
    answer = 0
    s = ''

    while n > 0:
        n, mod = divmod(n, k)
        s += str(mod)

    ans = s[::-1].split('0')

    for i in range(len(ans)):
        if not ans[i].isnumeric():
            continue
        x = int(ans[i])
        if x < 2:
            continue
        sosu = True
        for j in range(2, int(x ** 0.5)+1):
            if x % j == 0:
                sosu = False
                break
        if sosu:
            answer += 1

    return answer