def solution(strArr):
    answer = {}
    
    for x in strArr:
        if len(x) in answer:
            answer[len(x)] += 1
        else:
            answer[len(x)] = 1
            
    ans = sorted(answer.items(), key=lambda x: x[1], reverse=True)
    
    return ans[0][1]