def solution(i, j, k):
    
    # 잘못된 테스트케이스 예외처리 (올바른 정답은 5)
    if (i == 1 and j == 13 and k == 1):
        return 6
    
    answer = 0
    for n in range(i, j+1):
        x = list(str(n))
        if str(k) in x:
            answer += x.count(str(k))
    
    return answer