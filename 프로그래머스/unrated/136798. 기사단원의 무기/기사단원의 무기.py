def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number+1):
        ans = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                ans += 1
                if j != (i // j):
                    ans += 1
        if ans > limit:
            answer += power
        else:
            answer += ans
    
    return answer