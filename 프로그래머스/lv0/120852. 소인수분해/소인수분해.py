def solution(n):
    ans = 2
    answer = []
    
    while ans <= n:
        if (n % ans == 0):
            n /= ans
            if (ans not in answer):
                answer.append(ans)
        else:
            ans += 1

    return answer