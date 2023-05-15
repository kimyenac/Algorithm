def solution(ingredient):
    answer = 0
    ans = []
    
    for i in ingredient:
        ans.append(i)
        if ans[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                ans.pop()
    
    return answer