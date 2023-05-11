def solution(n):
    answer = []
    
    for i in range(n):
        ans = []
        for j in range(n):
            if i == j:
                ans.append(1)
            else:
                ans.append(0)
        answer.append(ans)
    
    return answer